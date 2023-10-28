# Licensed under a 3-clause BSD style license - see LICENSE
'''
Tests for the "counterpart_pairing" module.
'''

import os
import itertools
from numpy.testing import assert_allclose
import numpy as np
import pytest

from ..matching import CrossMatch
from ..counterpart_pairing import source_pairing
from ..counterpart_pairing_fortran import counterpart_pairing_fortran as cpf
from .test_matching import _replace_line


def test_calculate_contamination_probabilities():
    rho = np.linspace(0, 100, 10000)
    drho = np.diff(rho)

    sigs = np.array([0.1, 0.2, 0.3, 0.4])
    seed = 96473
    rng = np.random.default_rng(seed)
    G = np.empty((len(rho)-1, len(sigs)), float)
    for i in range(len(sigs)):
        G[:, i] = np.exp(-2 * np.pi**2 * (rho[:-1]+drho/2)**2 * sigs[i]**2)
    for sep in rng.uniform(0, 0.5, 10):
        Gcc, Gcn, Gnc, Gnn = cpf.contam_match_prob(
            G[:, 0], G[:, 1], G[:, 2], G[:, 3], rho[:-1]+drho/2, drho, sep)
        for prob, sig in zip([Gcc, Gcn, Gnc, Gnn], sigs):
            assert_allclose(prob, 1/(2*np.pi*sig**2) * np.exp(-0.5 * sep**2 / sig**2),
                            rtol=1e-3, atol=1e-4)


class TestCounterpartPairing:
    def setup_class(self):
        seed = 8888
        rng = np.random.default_rng(seed)
        # Test will have three overlap islands: two with 2 a sources and 1 b
        # source, with 1 unmatched a source, and one with 2 a + 1 b all unmatched
        # sources. Also two islands each with just one "field" object.
        self.a_astro = np.empty((7, 3), float)
        self.b_astro = np.empty((4, 3), float)
        self.a_sig, self.b_sig = 0.1, 0.08

        self.a_astro[:3, :2] = np.array([[0, 0], [0.1, 0.1], [0.1, 0]])
        self.a_astro[3:6, :2] = self.a_astro[:3, :2] + rng.choice([-1, 1], size=(3, 2)) * \
            rng.uniform(2.1*self.a_sig/3600, 3*self.a_sig/3600, size=(3, 2))
        self.a_astro[6, :2] = np.array([0.1, 0.1])
        # Force the second source in the island with the counterpart a/b pair
        # in "a" to be 2-3 sigma away, while the counterpart is <=1 sigma distant.
        self.b_astro[:3, :2] = self.a_astro[:3, :2] + \
            rng.uniform(-1*self.b_sig/3600, self.b_sig/3600, size=(3, 2))
        # Swap the first and second indexes around
        self.b_astro[:2, 0] = self.b_astro[[1, 0], 0]
        self.b_astro[:2, 1] = self.b_astro[[1, 0], 1]
        self.b_astro[-1, :2] = np.array([0.05, 0.05])
        # Swap the last two indexes as well
        self.b_astro[-2:, 0] = self.b_astro[[-1, -2], 0]
        self.b_astro[-2:, 1] = self.b_astro[[-1, -2], 1]
        # Force no match between the third island by adding distance between
        # a[2] and b[3]. Unphysical but effective.
        self.b_astro[3, 1] += 7*self.b_sig/3600

        self.a_astro[:, 2] = self.a_sig
        self.b_astro[:, 2] = self.b_sig
        # Currently we don't care about the photometry, setting both
        # include_phot_like and use_phot_priors to False, so just fake:
        self.a_photo = np.ones((7, 3), float)
        self.b_photo = np.ones((4, 4), float)

        self.alist = np.array([[0, 3], [1, 4], [2, 5], [6, -1], [-1, -1]]).T
        self.alist_ = self.alist
        self.blist = np.array([[1], [0], [3], [-1], [2]]).T
        self.blist_ = self.blist
        self.agrplen = np.array([2, 2, 2, 1, 0])
        self.bgrplen = np.array([1, 1, 1, 0, 1])

        self.rho = np.linspace(0, 100, 10000)
        self.drho = np.diff(self.rho)
        self.n_fracs = 2

        self.abinlengths = 2*np.ones((3, 1), int)
        self.bbinlengths = 2*np.ones((4, 1), int)
        # Having defaulted all photometry to a magnitude of 1, set bins:
        self.abinsarray = np.asfortranarray(np.broadcast_to(np.array([[[0]], [[2]]]), [2, 3, 1]))
        self.bbinsarray = np.asfortranarray(np.broadcast_to(np.array([[[0]], [[2]]]), [2, 4, 1]))
        self.c_array = np.ones((1, 1, 4, 3, 1), float, order='F')
        self.fa_array = np.ones((1, 4, 3, 1), float, order='F')
        self.fb_array = np.ones((1, 4, 3, 1), float, order='F')
        self.c_priors = np.asfortranarray((3/0.001**2 * 0.5) * np.ones((4, 3, 1), float))
        self.fa_priors = np.asfortranarray((7/0.001**2 - 3/0.001**2 * 0.5) *
                                           np.ones((4, 3, 1), float))
        self.fb_priors = np.asfortranarray((3/0.001**2 * 0.5) * np.ones((4, 3, 1), float))

        self.amagref = np.zeros((self.a_astro.shape[0]), int)
        self.bmagref = np.zeros((self.b_astro.shape[0]), int)

        self.amodelrefinds = np.zeros((3, 7), int, order='F')
        self.bmodelrefinds = np.zeros((3, 4), int, order='F')

        self.afrac_grids = np.zeros((self.n_fracs, 1, 3, 1), float, order='F')
        self.aflux_grids = np.zeros((1, 3, 1), float, order='F')
        self.bfrac_grids = np.zeros((self.n_fracs, 1, 4, 1), float, order='F')
        self.bflux_grids = np.zeros((1, 4, 1), float, order='F')
        self.afourier_grids = np.ones((len(self.rho)-1, 1, 3, 1), float, order='F')
        self.bfourier_grids = np.ones((len(self.rho)-1, 1, 4, 1), float, order='F')
        self.a_sky_inds = np.zeros((7), int)
        self.b_sky_inds = np.zeros((4), int)

        # We have to save various files for the source_pairing function to
        # pick up again.
        self.joint_folder_path = 'test_path'
        self.a_cat_folder_path = 'gaia_folder'
        self.b_cat_folder_path = 'wise_folder'
        self.a_auf_folder_path = 'gaia_auf_folder'
        self.b_auf_folder_path = 'wise_auf_folder'
        os.system('rm -r {}'.format(self.joint_folder_path))
        for f in ['pairing', 'phot_like', 'group']:
            os.makedirs('{}/{}'.format(self.joint_folder_path, f), exist_ok=True)
        for f in [self.a_cat_folder_path, self.b_cat_folder_path,
                  self.a_auf_folder_path, self.b_auf_folder_path]:
            os.makedirs(f, exist_ok=True)
        np.save('{}/con_cat_astro.npy'.format(self.a_cat_folder_path), self.a_astro)
        np.save('{}/con_cat_astro.npy'.format(self.b_cat_folder_path), self.b_astro)
        np.save('{}/con_cat_photo.npy'.format(self.a_cat_folder_path), self.a_photo)
        np.save('{}/con_cat_photo.npy'.format(self.b_cat_folder_path), self.b_photo)
        np.save('{}/magref.npy'.format(self.a_cat_folder_path), self.amagref)
        np.save('{}/magref.npy'.format(self.b_cat_folder_path), self.bmagref)

        np.save('{}/group/alist.npy'.format(self.joint_folder_path), self.alist)
        np.save('{}/group/blist.npy'.format(self.joint_folder_path), self.blist)
        np.save('{}/group/agrplen.npy'.format(self.joint_folder_path), self.agrplen)
        np.save('{}/group/bgrplen.npy'.format(self.joint_folder_path), self.bgrplen)

        np.save('{}/phot_like/abinsarray.npy'.format(self.joint_folder_path), self.abinsarray)
        np.save('{}/phot_like/bbinsarray.npy'.format(self.joint_folder_path), self.bbinsarray)
        np.save('{}/phot_like/abinlengths.npy'.format(self.joint_folder_path), self.abinlengths)
        np.save('{}/phot_like/bbinlengths.npy'.format(self.joint_folder_path), self.bbinlengths)

        np.save('{}/phot_like/c_priors.npy'.format(self.joint_folder_path), self.c_priors)
        np.save('{}/phot_like/c_array.npy'.format(self.joint_folder_path), self.c_array)
        np.save('{}/phot_like/fa_priors.npy'.format(self.joint_folder_path), self.fa_priors)
        np.save('{}/phot_like/fa_array.npy'.format(self.joint_folder_path), self.fa_array)
        np.save('{}/phot_like/fb_priors.npy'.format(self.joint_folder_path), self.fb_priors)
        np.save('{}/phot_like/fb_array.npy'.format(self.joint_folder_path), self.fb_array)

        np.save('{}/phot_like/a_sky_inds.npy'.format(self.joint_folder_path), self.a_sky_inds)
        np.save('{}/phot_like/b_sky_inds.npy'.format(self.joint_folder_path), self.b_sky_inds)

        np.save('{}/modelrefinds.npy'.format(self.a_auf_folder_path), self.amodelrefinds)
        np.save('{}/modelrefinds.npy'.format(self.b_auf_folder_path), self.bmodelrefinds)

        np.save('{}/arraylengths.npy'.format(self.a_auf_folder_path), np.ones((3, 1), int))
        np.save('{}/arraylengths.npy'.format(self.b_auf_folder_path), np.ones((4, 1), int))

        # We should have already made fourier_grid, frac_grid, and flux_grid
        # for each catalogue.
        np.save('{}/fourier_grid.npy'.format(self.a_auf_folder_path), self.afourier_grids)
        np.save('{}/fourier_grid.npy'.format(self.b_auf_folder_path), self.bfourier_grids)
        np.save('{}/frac_grid.npy'.format(self.a_auf_folder_path), self.afrac_grids)
        np.save('{}/frac_grid.npy'.format(self.b_auf_folder_path), self.bfrac_grids)
        np.save('{}/flux_grid.npy'.format(self.a_auf_folder_path), self.aflux_grids)
        np.save('{}/flux_grid.npy'.format(self.b_auf_folder_path), self.bflux_grids)

        self.a_auf_pointings = np.array([[0.0, 0.0]])
        self.b_auf_pointings = np.array([[0.0, 0.0]])
        self.a_filt_names = np.array(['G_BP', 'G', 'G_RP'])
        self.b_filt_names = np.array(['W1', 'W2', 'W3', 'W4'])

        self.large_len = max(len(self.a_astro), len(self.b_astro))

    def _calculate_prob_integral(self):
        self.o = np.sqrt(self.a_sig**2 + self.b_sig**2) / 3600
        self.sep = np.sqrt(((self.a_astro[0, 0] -
                             self.b_astro[1, 0])*np.cos(np.radians(self.b_astro[1, 1])))**2 +
                           (self.a_astro[0, 1] - self.b_astro[1, 1])**2)
        self.G = 1/(2 * np.pi * self.o**2) * np.exp(-0.5 * self.sep**2 / self.o**2)
        self.sep_wrong = np.sqrt(((self.a_astro[3, 0] -
                                   self.b_astro[1, 0])*np.cos(np.radians(self.a_astro[3, 1])))**2 +
                                 (self.a_astro[3, 1] - self.b_astro[1, 1])**2)
        self.G_wrong = 1/(2 * np.pi * self.o**2) * np.exp(-0.5 * self.sep_wrong**2 / self.o**2)
        self.Nc = self.c_priors[0, 0, 0]
        self.Nfa, self.Nfb = self.fa_priors[0, 0, 0], self.fb_priors[0, 0, 0]

    def test_individual_island_probability(self):
        os.system('rm -r {}/pairing'.format(self.joint_folder_path))
        os.makedirs('{}/pairing'.format(self.joint_folder_path), exist_ok=True)
        i = 0
        wrapper = [
            self.a_astro, self.a_photo, self.b_astro, self.b_photo, self.c_array, self.fa_array,
            self.fb_array, self.c_priors, self.fa_priors, self.fb_priors, self.abinsarray,
            self.bbinsarray, self.abinlengths, self.bbinlengths, self.afrac_grids,
            self.aflux_grids, self.afourier_grids, self.bfrac_grids, self.bflux_grids,
            self.bfourier_grids, self.rho, self.drho, self.n_fracs, self.large_len,
            self.alist[:self.agrplen[i], i]+1, self.blist[:self.bgrplen[i], i]+1,
            self.alist_[:self.agrplen[i], i], self.blist_[:self.bgrplen[i], i],
            self.amagref[self.alist[:self.agrplen[i], i]]+1,
            self.a_sky_inds[self.alist[:self.agrplen[i], i]]+1,
            self.bmagref[self.blist[:self.bgrplen[i], i]]+1,
            self.b_sky_inds[self.blist[:self.bgrplen[i], i]]+1,
            self.amodelrefinds[:, self.alist[:self.agrplen[i], i]]+1,
            self.bmodelrefinds[:, self.blist[:self.bgrplen[i], i]]+1]
        results = cpf.find_single_island_prob(*wrapper)

        (acrpts, bcrpts, acrptscontp, bcrptscontp, etacrpts, xicrpts, acrptflux, bcrptflux,
         crptseps, afield, bfield, afieldflux, bfieldflux, afieldseps, afieldeta,
         afieldxi, bfieldseps, bfieldeta, bfieldxi, prob, integral) = results

        assert np.all(acrpts == np.array([0]))
        assert np.all(bcrpts == np.array([1]))
        assert np.all(acrptscontp == np.array([0]))
        assert np.all(bcrptscontp == np.array([0]))
        assert np.all(etacrpts == np.array([0]))

        self._calculate_prob_integral()
        assert_allclose(xicrpts, np.array([np.log10(self.G / self.fa_priors[0, 0, 0])]), rtol=1e-6)
        assert np.all(acrptflux == np.array([0]))
        assert np.all(bcrptflux == np.array([0]))
        # 2 a vs 1 b with a match means only one rejected a source, but a
        # length 2 array; similarly, bfield will be empty but length one.
        assert np.all(afield == np.array([3, self.large_len+1]))
        assert len(bfield) == 1
        assert np.all(bfield == np.array([self.large_len+1]))

        _integral = self.Nc*self.G*self.Nfa + self.Nc*self.G_wrong*self.Nfa +\
            self.Nfa*self.Nfa*self.Nfb
        assert_allclose(integral, _integral, rtol=1e-5)
        _prob = self.Nc*self.G*self.Nfa
        assert_allclose(prob, _prob, rtol=1e-5)

    def test_individual_island_zero_probabilities(self):
        os.system('rm -r {}/pairing'.format(self.joint_folder_path))
        os.makedirs('{}/pairing'.format(self.joint_folder_path), exist_ok=True)
        # Fake the extra fire extinguisher likelihood/prior used in the main code.
        fa_array = np.zeros_like(self.fa_array) + 1e-10
        fb_array = np.zeros_like(self.fb_array) + 1e-10
        fa_priors = np.zeros_like(self.fa_priors) + 1e-10
        fb_priors = np.zeros_like(self.fb_priors) + 1e-10
        i = 0
        wrapper = [
            self.a_astro, self.a_photo, self.b_astro, self.b_photo, self.c_array, fa_array,
            fb_array, self.c_priors, fa_priors, fb_priors, self.abinsarray,
            self.bbinsarray, self.abinlengths, self.bbinlengths, self.afrac_grids,
            self.aflux_grids, self.afourier_grids, self.bfrac_grids, self.bflux_grids,
            self.bfourier_grids, self.rho, self.drho, self.n_fracs, self.large_len,
            self.alist[:self.agrplen[i], i]+1, self.blist[:self.bgrplen[i], i]+1,
            self.alist_[:self.agrplen[i], i], self.blist_[:self.bgrplen[i], i],
            self.amagref[self.alist[:self.agrplen[i], i]]+1,
            self.a_sky_inds[self.alist[:self.agrplen[i], i]]+1,
            self.bmagref[self.blist[:self.bgrplen[i], i]]+1,
            self.b_sky_inds[self.blist[:self.bgrplen[i], i]]+1,
            self.amodelrefinds[:, self.alist[:self.agrplen[i], i]]+1,
            self.bmodelrefinds[:, self.blist[:self.bgrplen[i], i]]+1]
        results = cpf.find_single_island_prob(*wrapper)
        (acrpts, bcrpts, acrptscontp, bcrptscontp, etacrpts, xicrpts, acrptflux, bcrptflux,
         crptseps, afield, bfield, afieldflux, bfieldflux, afieldseps, afieldeta,
         afieldxi, bfieldseps, bfieldeta, bfieldxi, prob, integral) = results

        assert np.all(acrpts == np.array([0]))
        assert np.all(bcrpts == np.array([1]))

        c_array = np.zeros_like(self.c_array) + 1e-10
        c_priors = np.zeros_like(self.c_priors) + 1e-10
        wrapper = [
            self.a_astro, self.a_photo, self.b_astro, self.b_photo, c_array, fa_array,
            fb_array, c_priors, fa_priors, fb_priors, self.abinsarray,
            self.bbinsarray, self.abinlengths, self.bbinlengths, self.afrac_grids,
            self.aflux_grids, self.afourier_grids, self.bfrac_grids, self.bflux_grids,
            self.bfourier_grids, self.rho, self.drho, self.n_fracs, self.large_len,
            self.alist[:self.agrplen[i], i]+1, self.blist[:self.bgrplen[i], i]+1,
            self.alist_[:self.agrplen[i], i], self.blist_[:self.bgrplen[i], i],
            self.amagref[self.alist[:self.agrplen[i], i]]+1,
            self.a_sky_inds[self.alist[:self.agrplen[i], i]]+1,
            self.bmagref[self.blist[:self.bgrplen[i], i]]+1,
            self.b_sky_inds[self.blist[:self.bgrplen[i], i]]+1,
            self.amodelrefinds[:, self.alist[:self.agrplen[i], i]]+1,
            self.bmodelrefinds[:, self.blist[:self.bgrplen[i], i]]+1]
        results = cpf.find_single_island_prob(*wrapper)
        (acrpts, bcrpts, acrptscontp, bcrptscontp, etacrpts, xicrpts, acrptflux, bcrptflux,
         crptseps, afield, bfield, afieldflux, bfieldflux, afieldseps, afieldeta,
         afieldxi, bfieldseps, bfieldeta, bfieldxi, prob, integral) = results

        assert len(acrpts) == 1
        assert len(bcrpts) == 1
        assert np.all(acrpts == np.array([self.large_len+1]))
        assert np.all(bcrpts == np.array([self.large_len+1]))
        assert_allclose(prob/integral, 1)

    def test_source_pairing(self):
        os.system('rm -r {}/pairing'.format(self.joint_folder_path))
        os.makedirs('{}/pairing'.format(self.joint_folder_path), exist_ok=True)
        mem_chunk_num = 2
        a_modelrefinds = None
        b_moderefinds = None
        source_pairing(
            self.joint_folder_path, self.a_cat_folder_path, self.b_cat_folder_path,
            self.a_auf_folder_path, self.b_auf_folder_path, self.a_filt_names, self.b_filt_names,
            self.a_auf_pointings, self.b_auf_pointings, a_modelrefinds, b_moderefinds,
            self.rho, self.drho, self.n_fracs, mem_chunk_num, group_sources_data=None,
            phot_like_data=None, use_memmap_files=True)

        bflux = np.load('{}/pairing/bcontamflux.npy'.format(self.joint_folder_path))
        assert np.all(bflux == np.zeros((2), float))

        aflux = np.load('{}/pairing/afieldflux.npy'.format(self.joint_folder_path))
        assert np.all(aflux == np.zeros((5), float))
        bflux = np.load('{}/pairing/bfieldflux.npy'.format(self.joint_folder_path))
        assert np.all(bflux == np.zeros((2), float))

        a_matches = np.load('{}/pairing/ac.npy'.format(self.joint_folder_path))
        assert np.all([q in a_matches for q in [0, 1]])
        assert np.all([q not in a_matches for q in [2, 3, 4, 5, 6]])

        a_field = np.load('{}/pairing/af.npy'.format(self.joint_folder_path))
        assert np.all([q in a_field for q in [2, 3, 4, 5, 6]])
        assert np.all([q not in a_field for q in [0, 1]])

        b_matches = np.load('{}/pairing/bc.npy'.format(self.joint_folder_path))
        assert np.all([q in b_matches for q in [0, 1]])
        assert np.all([q not in b_matches for q in [2, 3]])

        b_field = np.load('{}/pairing/bf.npy'.format(self.joint_folder_path))
        assert np.all([q in b_field for q in [2, 3]])
        assert np.all([q not in b_field for q in [0, 1]])

        prob_counterpart = np.load('{}/pairing/pc.npy'.format(self.joint_folder_path))
        self._calculate_prob_integral()
        _integral = self.Nc*self.G*self.Nfa + self.Nc*self.G_wrong*self.Nfa +\
            self.Nfa*self.Nfa*self.Nfb
        _prob = self.Nc*self.G*self.Nfa
        norm_prob = _prob/_integral
        q = np.where(a_matches == 0)[0][0]
        assert_allclose(prob_counterpart[q], norm_prob, rtol=1e-5)
        xicrpts = np.load('{}/pairing/xi.npy'.format(self.joint_folder_path))
        assert_allclose(xicrpts[q], np.array([np.log10(self.G / self.fa_priors[0, 0, 0])]),
                        rtol=1e-6)
        csep = np.load('{}/pairing/crptseps.npy'.format(self.joint_folder_path))
        assert_allclose(csep[q], self.sep * 3600, rtol=1e-6)
        assert len(csep) == len(a_matches)

        prob_a_field = np.load('{}/pairing/pfa.npy'.format(self.joint_folder_path))
        a_field = np.load('{}/pairing/af.npy'.format(self.joint_folder_path))
        q = np.where(a_field == 6)[0][0]
        assert prob_a_field[q] == 1

        prob_b_field = np.load('{}/pairing/pfb.npy'.format(self.joint_folder_path))
        b_field = np.load('{}/pairing/bf.npy'.format(self.joint_folder_path))
        q = np.where(b_field == 2)[0][0]
        assert prob_b_field[q] == 1

        afs = np.load('{}/pairing/afieldseps.npy'.format(self.joint_folder_path))
        afeta = np.load('{}/pairing/afieldeta.npy'.format(self.joint_folder_path))
        afxi = np.load('{}/pairing/afieldxi.npy'.format(self.joint_folder_path))
        q = np.where(a_field == 2)[0][0]
        fake_field_sep = np.sqrt(((self.a_astro[2, 0] -
                                   self.b_astro[3, 0])*np.cos(np.radians(self.b_astro[3, 1])))**2 +
                                 (self.a_astro[2, 1] - self.b_astro[3, 1])**2)
        assert_allclose(afs[q], fake_field_sep * 3600, rtol=1e-6)

        fake_field_G = 1/(2 * np.pi * self.o**2) * np.exp(-0.5 * fake_field_sep**2 / self.o**2)
        # c_priors and fb_priors are the same, so they cancel in the division.
        # Being in log space we can be relatively forgiving in our assertion limits.
        assert_allclose(afxi[q], np.log10(fake_field_G / self.Nfa), rtol=0.01, atol=0.01)
        # Ignoring photometry here, so this should be equal probability.
        assert_allclose(afeta[q], np.log10(1.0))

    def test_including_b_reject(self):
        os.system('rm -r {}/pairing'.format(self.joint_folder_path))
        os.makedirs('{}/pairing'.format(self.joint_folder_path), exist_ok=True)
        # Remove the third group, pretending it's rejected in the group stage.
        alist = self.alist[:, [0, 1, 3, 4]]
        blist = self.blist[:, [0, 1, 3, 4]]
        agrplen = self.agrplen[[0, 1, 3, 4]]
        bgrplen = self.bgrplen[[0, 1, 3, 4]]

        a_reject = np.array([2, 5])
        b_reject = np.array([3])
        os.system('rm -r {}/reject'.format(self.joint_folder_path))
        os.makedirs('{}/reject'.format(self.joint_folder_path), exist_ok=True)
        np.save('{}/reject/reject_a.npy'.format(self.joint_folder_path), a_reject)
        np.save('{}/reject/reject_b.npy'.format(self.joint_folder_path), b_reject)

        np.save('{}/group/alist.npy'.format(self.joint_folder_path), alist)
        np.save('{}/group/blist.npy'.format(self.joint_folder_path), blist)
        np.save('{}/group/agrplen.npy'.format(self.joint_folder_path), agrplen)
        np.save('{}/group/bgrplen.npy'.format(self.joint_folder_path), bgrplen)

        mem_chunk_num = 2
        a_modelrefinds = None
        b_moderefinds = None
        source_pairing(
            self.joint_folder_path, self.a_cat_folder_path, self.b_cat_folder_path,
            self.a_auf_folder_path, self.b_auf_folder_path, self.a_filt_names,
            self.b_filt_names, self.a_auf_pointings, self.b_auf_pointings, a_modelrefinds, b_moderefinds,
            self.rho, self.drho, self.n_fracs, mem_chunk_num, group_sources_data=None, phot_like_data=None,
            use_memmap_files=True)

        bflux = np.load('{}/pairing/bcontamflux.npy'.format(self.joint_folder_path))
        assert np.all(bflux == np.zeros((2), float))

        a_matches = np.load('{}/pairing/ac.npy'.format(self.joint_folder_path))
        assert np.all([q in a_matches for q in [0, 1]])
        assert np.all([q not in a_matches for q in [2, 3, 4, 5, 6]])

        a_field = np.load('{}/pairing/af.npy'.format(self.joint_folder_path))
        assert np.all([q in a_field for q in [3, 4, 6]])
        assert np.all([q not in a_field for q in [0, 1, 2, 5]])

        b_matches = np.load('{}/pairing/bc.npy'.format(self.joint_folder_path))
        assert np.all([q in b_matches for q in [0, 1]])
        assert np.all([q not in b_matches for q in [2, 3]])

        b_field = np.load('{}/pairing/bf.npy'.format(self.joint_folder_path))
        assert np.all([q in b_field for q in [2]])
        assert np.all([q not in b_field for q in [0, 1, 3]])

        prob_counterpart = np.load('{}/pairing/pc.npy'.format(self.joint_folder_path))
        self._calculate_prob_integral()
        _integral = self.Nc*self.G*self.Nfa + self.Nc*self.G_wrong*self.Nfa + \
            self.Nfa*self.Nfa*self.Nfb
        _prob = self.Nc*self.G*self.Nfa
        norm_prob = _prob/_integral
        q = np.where(a_matches == 0)[0][0]
        assert_allclose(prob_counterpart[q], norm_prob, rtol=1e-5)
        xicrpts = np.load('{}/pairing/xi.npy'.format(self.joint_folder_path))
        assert_allclose(xicrpts[q], np.array([np.log10(self.G / self.fa_priors[0, 0, 0])]),
                        rtol=1e-6)

        prob_a_field = np.load('{}/pairing/pfa.npy'.format(self.joint_folder_path))
        a_field = np.load('{}/pairing/af.npy'.format(self.joint_folder_path))
        q = np.where(a_field == 6)[0][0]
        assert prob_a_field[q] == 1

        prob_b_field = np.load('{}/pairing/pfb.npy'.format(self.joint_folder_path))
        b_field = np.load('{}/pairing/bf.npy'.format(self.joint_folder_path))
        q = np.where(b_field == 2)[0][0]
        assert prob_b_field[q] == 1

    def test_small_length_warnings(self):
        os.system('rm -r {}/pairing'.format(self.joint_folder_path))
        os.makedirs('{}/pairing'.format(self.joint_folder_path), exist_ok=True)
        os.makedirs('{}/reject'.format(self.joint_folder_path), exist_ok=True)
        # Here want to test that the number of recorded matches -- either
        # counterpart, field, or rejected -- is lower than the total length.
        # To achieve this we fake reject length arrays smaller than their
        # supposed lengths.
        alist = self.alist[:, [0, 1, 4]]
        blist = self.blist[:, [0, 1, 4]]
        agrplen = self.agrplen[[0, 1, 4]]
        bgrplen = self.bgrplen[[0, 1, 4]]

        # Force catalogue a to have the wrong length by simply leaving a group
        # out of alist.
        a_reject = np.array([6])
        np.save('{}/reject/reject_a.npy'.format(self.joint_folder_path), a_reject)
        os.system('rm {}/reject/reject_b.npy'.format(self.joint_folder_path))

        np.save('{}/group/alist.npy'.format(self.joint_folder_path), alist)
        np.save('{}/group/blist.npy'.format(self.joint_folder_path), blist)
        np.save('{}/group/agrplen.npy'.format(self.joint_folder_path), agrplen)
        np.save('{}/group/bgrplen.npy'.format(self.joint_folder_path), bgrplen)

        mem_chunk_num = 2
        a_modelrefinds = None
        b_moderefinds = None
        with pytest.warns(UserWarning) as record:
            source_pairing(
                self.joint_folder_path, self.a_cat_folder_path, self.b_cat_folder_path,
                self.a_auf_folder_path, self.b_auf_folder_path, self.a_filt_names,
                self.b_filt_names, self.a_auf_pointings, self.b_auf_pointings, a_modelrefinds, b_moderefinds,
                self.rho, self.drho, self.n_fracs, mem_chunk_num, group_sources_data=None, phot_like_data=None,
                use_memmap_files=True)
        assert len(record) == 2
        assert '2 catalogue a sources not in either counterpart, f' in record[0].message.args[0]
        assert '1 catalogue b source not in either counterpart, f' in record[1].message.args[0]

        bflux = np.load('{}/pairing/bcontamflux.npy'.format(self.joint_folder_path))
        assert np.all(bflux == np.zeros((2), float))

        a_matches = np.load('{}/pairing/ac.npy'.format(self.joint_folder_path))
        assert np.all([q in a_matches for q in [0, 1]])
        assert np.all([q not in a_matches for q in [2, 3, 4, 5, 6]])

        a_field = np.load('{}/pairing/af.npy'.format(self.joint_folder_path))
        assert np.all([q in a_field for q in [3, 4]])
        assert np.all([q not in a_field for q in [0, 1, 2, 5, 6]])

        a_reject = np.load('{}/reject/reject_a.npy'.format(self.joint_folder_path))
        assert np.all([q in a_reject for q in [6]])
        assert np.all([q not in a_reject for q in [0, 1, 2, 3, 4, 5]])

        b_matches = np.load('{}/pairing/bc.npy'.format(self.joint_folder_path))
        assert np.all([q in b_matches for q in [0, 1]])
        assert np.all([q not in b_matches for q in [2, 3]])

        b_field = np.load('{}/pairing/bf.npy'.format(self.joint_folder_path))
        assert np.all([q in b_field for q in [2]])
        assert np.all([q not in b_field for q in [0, 1, 3]])

    def test_large_length_warnings(self):
        os.system('rm -r {}/pairing'.format(self.joint_folder_path))
        os.makedirs('{}/pairing'.format(self.joint_folder_path), exist_ok=True)
        os.makedirs('{}/reject'.format(self.joint_folder_path), exist_ok=True)
        # Here want to test that the number of recorded matches -- either
        # counterpart, field, or rejected -- is higher than the total length.
        # To achieve this we fake reject length arrays larger than their
        # supposed lengths.
        alist = self.alist[:, [0, 1, 4]]
        blist = self.blist[:, [0, 1, 4]]
        agrplen = self.agrplen[[0, 1, 4]]
        bgrplen = self.bgrplen[[0, 1, 4]]

        a_reject = np.array([2, 3, 4, 5, 6])
        b_reject = np.array([1, 3])
        np.save('{}/reject/reject_a.npy'.format(self.joint_folder_path), a_reject)
        np.save('{}/reject/reject_b.npy'.format(self.joint_folder_path), b_reject)

        np.save('{}/group/alist.npy'.format(self.joint_folder_path), alist)
        np.save('{}/group/blist.npy'.format(self.joint_folder_path), blist)
        np.save('{}/group/agrplen.npy'.format(self.joint_folder_path), agrplen)
        np.save('{}/group/bgrplen.npy'.format(self.joint_folder_path), bgrplen)

        mem_chunk_num = 2
        a_modelrefinds = None
        b_moderefinds = None
        with pytest.warns(UserWarning) as record:
            source_pairing(
                self.joint_folder_path, self.a_cat_folder_path, self.b_cat_folder_path,
                self.a_auf_folder_path, self.b_auf_folder_path, self.a_filt_names,
                self.b_filt_names, self.a_auf_pointings, self.b_auf_pointings, a_modelrefinds, b_moderefinds,
                self.rho, self.drho, self.n_fracs, mem_chunk_num, group_sources_data=None, phot_like_data=None,
                use_memmap_files=True)
        assert len(record) == 2
        assert '2 additional catalogue a indices recorded' in record[0].message.args[0]
        assert '1 additional catalogue b index recorded' in record[1].message.args[0]

        bflux = np.load('{}/pairing/bcontamflux.npy'.format(self.joint_folder_path))
        assert np.all(bflux == np.zeros((2), float))

        a_matches = np.load('{}/pairing/ac.npy'.format(self.joint_folder_path))
        assert np.all([q in a_matches for q in [0, 1]])
        assert np.all([q not in a_matches for q in [2, 3, 4, 5, 6]])

        a_field = np.load('{}/pairing/af.npy'.format(self.joint_folder_path))
        assert np.all([q in a_field for q in [3, 4]])
        assert np.all([q not in a_field for q in [0, 1, 2, 5, 6]])

        a_reject = np.load('{}/reject/reject_a.npy'.format(self.joint_folder_path))
        assert np.all([q in a_reject for q in [2, 3, 4, 5, 6]])
        assert np.all([q not in a_reject for q in [0, 1]])

        b_matches = np.load('{}/pairing/bc.npy'.format(self.joint_folder_path))
        assert np.all([q in b_matches for q in [0, 1]])
        assert np.all([q not in b_matches for q in [2, 3]])

        b_field = np.load('{}/pairing/bf.npy'.format(self.joint_folder_path))
        assert np.all([q in b_field for q in [2]])
        assert np.all([q not in b_field for q in [0, 1, 3]])

    def _setup_cross_match_parameters(self):
        # Ensure output chunk directory exists
        os.makedirs(os.path.join(os.path.dirname(__file__), "data/chunk0"), exist_ok=True)

        for ol, nl in zip(['cf_region_points = 131 134 4 -1 1 3', 'mem_chunk_num = 10'],
                          ['cf_region_points = 131 131 1 0 0 1\n', 'mem_chunk_num = 2\n']):
            f = open(os.path.join(os.path.dirname(__file__),
                                  'data/crossmatch_params.txt')).readlines()
            idx = np.where([ol in line for line in f])[0][0]
            _replace_line(os.path.join(os.path.dirname(__file__), 'data/crossmatch_params.txt'),
                          idx, nl, out_file=os.path.join(os.path.dirname(__file__),
                          'data/chunk0/crossmatch_params_.txt'))

        ol, nl = 'auf_region_points = 131 134 4 -1 1 {}', 'auf_region_points = 0 0 1 0 0 1\n'
        for file_name in ['cat_a_params', 'cat_b_params']:
            _ol = ol.format('3' if '_a_' in file_name else '4')
            f = open(os.path.join(os.path.dirname(__file__),
                                  'data/{}.txt'.format(file_name))).readlines()
            idx = np.where([_ol in line for line in f])[0][0]
            _replace_line(os.path.join(os.path.dirname(__file__), 'data/{}.txt'.format(file_name)),
                          idx, nl, out_file=os.path.join(os.path.dirname(__file__),
                          'data/chunk0/{}_.txt'.format(file_name)))

    def test_pair_sources(self):
        os.system('rm -r {}/pairing'.format(self.joint_folder_path))
        os.makedirs('{}/pairing'.format(self.joint_folder_path), exist_ok=True)
        os.system('rm -r {}/reject/*'.format(self.joint_folder_path))
        np.save('{}/group/alist.npy'.format(self.joint_folder_path), self.alist)
        np.save('{}/group/blist.npy'.format(self.joint_folder_path), self.blist)
        np.save('{}/group/agrplen.npy'.format(self.joint_folder_path), self.agrplen)
        np.save('{}/group/bgrplen.npy'.format(self.joint_folder_path), self.bgrplen)
        # Same run as test_source_pairing, but called from CrossMatch rather than
        # directly this time.
        self._setup_cross_match_parameters()
        self.cm = CrossMatch(os.path.join(os.path.dirname(__file__), 'data'), use_memmap_files=True)
        self.cm.delta_mag_cuts = np.array([2.5, 5])
        self.cm.a_modelrefinds = None
        self.cm.b_modelrefinds = None
        self.cm.group_sources_data = None
        self.cm.phot_like_data = None
        self.files_per_pairing = 13
        self.cm.chunk_id = 1
        self.cm._initialise_chunk(os.path.join(os.path.dirname(__file__), 'data/chunk0/crossmatch_params_.txt'),
                                  os.path.join(os.path.dirname(__file__), 'data/chunk0/cat_a_params_.txt'),
                                  os.path.join(os.path.dirname(__file__), 'data/chunk0/cat_b_params_.txt'))
        self.cm.pair_sources(self.files_per_pairing)

        bflux = np.load('{}/pairing/bcontamflux.npy'.format(self.joint_folder_path))
        assert np.all(bflux == np.zeros((2), float))

        a_matches = np.load('{}/pairing/ac.npy'.format(self.joint_folder_path))
        assert np.all([q in a_matches for q in [0, 1]])
        assert np.all([q not in a_matches for q in [2, 3, 4, 5, 6]])

        a_field = np.load('{}/pairing/af.npy'.format(self.joint_folder_path))
        assert np.all([q in a_field for q in [2, 3, 4, 5, 6]])
        assert np.all([q not in a_field for q in [0, 1]])

        b_matches = np.load('{}/pairing/bc.npy'.format(self.joint_folder_path))
        assert np.all([q in b_matches for q in [0, 1]])
        assert np.all([q not in b_matches for q in [2, 3]])

        b_field = np.load('{}/pairing/bf.npy'.format(self.joint_folder_path))
        assert np.all([q in b_field for q in [2, 3]])
        assert np.all([q not in b_field for q in [0, 1]])

        prob_counterpart = np.load('{}/pairing/pc.npy'.format(self.joint_folder_path))
        self._calculate_prob_integral()
        _integral = self.Nc*self.G*self.Nfa + self.Nc*self.G_wrong*self.Nfa + \
            self.Nfa*self.Nfa*self.Nfb
        _prob = self.Nc*self.G*self.Nfa
        norm_prob = _prob/_integral
        q = np.where(a_matches == 0)[0][0]
        assert_allclose(prob_counterpart[q], norm_prob, rtol=1e-5)
        xicrpts = np.load('{}/pairing/xi.npy'.format(self.joint_folder_path))
        assert_allclose(xicrpts[q], np.array([np.log10(self.G / self.fa_priors[0, 0, 0])]),
                        rtol=1e-6)

        prob_a_field = np.load('{}/pairing/pfa.npy'.format(self.joint_folder_path))
        a_field = np.load('{}/pairing/af.npy'.format(self.joint_folder_path))
        q = np.where(a_field == 6)[0][0]
        assert prob_a_field[q] == 1

        prob_b_field = np.load('{}/pairing/pfb.npy'.format(self.joint_folder_path))
        b_field = np.load('{}/pairing/bf.npy'.format(self.joint_folder_path))
        q = np.where(b_field == 2)[0][0]
        assert prob_b_field[q] == 1

        afs = np.load('{}/pairing/afieldseps.npy'.format(self.joint_folder_path))
        afeta = np.load('{}/pairing/afieldeta.npy'.format(self.joint_folder_path))
        afxi = np.load('{}/pairing/afieldxi.npy'.format(self.joint_folder_path))
        q = np.where(a_field == 2)[0][0]
        fake_field_sep = np.sqrt(((self.a_astro[2, 0] -
                                   self.b_astro[3, 0])*np.cos(np.radians(self.b_astro[3, 1])))**2 +
                                 (self.a_astro[2, 1] - self.b_astro[3, 1])**2)
        assert_allclose(afs[q], fake_field_sep * 3600, rtol=1e-6)

        fake_field_G = 1/(2 * np.pi * self.o**2) * np.exp(-0.5 * fake_field_sep**2 / self.o**2)
        # c_priors and fb_priors are the same, so they cancel in the division.
        # Being in log space we can be relatively forgiving in our assertion limits.
        assert_allclose(afxi[q], np.log10(fake_field_G / self.Nfa), rtol=0.01, atol=0.01)
        # Ignoring photometry here, so this should be equal probability.
        assert_allclose(afeta[q], np.log10(1.0))

    def test_pair_sources_incorrect_warning(self):
        os.system('rm -r {}/pairing'.format(self.joint_folder_path))
        os.makedirs('{}/pairing'.format(self.joint_folder_path), exist_ok=True)
        self._setup_cross_match_parameters()
        for kind in ['cf', 'source']:
            ol, nl = 'run_{} = yes'.format(kind), 'run_{} = no\n'.format(kind)
            f = open(os.path.join(os.path.dirname(__file__),
                                  'data/crossmatch_params.txt')).readlines()
            idx = np.where([ol in line for line in f])[0][0]
            _replace_line(os.path.join(os.path.dirname(__file__),
                          'data/chunk0/crossmatch_params_.txt'), idx, nl)
        self.cm = CrossMatch(os.path.join(os.path.dirname(__file__), 'data'), use_memmap_files=True)
        self.cm.delta_mag_cuts = np.array([2.5, 5])
        self.cm.a_modelrefinds = None
        self.cm.b_modelrefinds = None
        self.cm.group_sources_data = None
        self.cm.phot_like_data = None
        self.files_per_pairing = 13
        self.cm.chunk_id = 1
        self.cm._initialise_chunk(os.path.join(os.path.dirname(__file__), 'data/chunk0/crossmatch_params_.txt'),
                                  os.path.join(os.path.dirname(__file__), 'data/chunk0/cat_a_params_.txt'),
                                  os.path.join(os.path.dirname(__file__), 'data/chunk0/cat_b_params_.txt'))
        with pytest.warns(UserWarning, match="Incorrect number of counterpart pairing files."):
            self.cm.pair_sources(self.files_per_pairing)

    def test_pair_sources_load_existing(self, capsys):
        os.system('rm -r {}/pairing'.format(self.joint_folder_path))
        os.makedirs('{}/pairing'.format(self.joint_folder_path), exist_ok=True)
        # Fake files_per_pairing sources at random.
        self.files_per_pairing = 13
        for i in range(0, self.files_per_pairing):
            np.save('{}/pairing/array_{}.npy'.format(self.joint_folder_path, i+1),
                    np.zeros((4, 3), float))

        self._setup_cross_match_parameters()
        for kind in ['cf', 'source']:
            ol, nl = 'run_{} = yes'.format(kind), 'run_{} = no\n'.format(kind)
            f = open(os.path.join(os.path.dirname(__file__),
                                  'data/crossmatch_params.txt')).readlines()
            idx = np.where([ol in line for line in f])[0][0]
            _replace_line(os.path.join(os.path.dirname(__file__),
                          'data/chunk0/crossmatch_params_.txt'), idx, nl)
        self.cm = CrossMatch(os.path.join(os.path.dirname(__file__), 'data'), use_memmap_files=True)
        self.cm.delta_mag_cuts = np.array([2.5, 5])
        self.cm.a_modelrefinds = None
        self.cm.b_modelrefinds = None
        self.cm.group_sources_data = None
        self.cm.phot_like_data = None
        self.cm.chunk_id = 1
        self.cm._initialise_chunk(os.path.join(os.path.dirname(__file__), 'data/chunk0/crossmatch_params_.txt'),
                                  os.path.join(os.path.dirname(__file__), 'data/chunk0/cat_a_params_.txt'),
                                  os.path.join(os.path.dirname(__file__), 'data/chunk0/cat_b_params_.txt'))
        capsys.readouterr()
        self.cm.pair_sources(self.files_per_pairing)
        output = capsys.readouterr().out
        assert 'Loading pre-assigned counterparts' in output


def test_f90_comb():
    for n in [2, 3, 4, 5]:
        for k in range(2, n+1, 1):
            n_combs = np.math.factorial(n) / np.math.factorial(k) / np.math.factorial(n - k)
            combs = cpf.calc_combs(n, n_combs, k).T
            new_combs = combs[np.lexsort([combs[:, i] for i in range(k)])]

            iter_combs = np.array(list(itertools.combinations(np.arange(1, n+1, 1), k)))
            new_iter_combs = iter_combs[np.lexsort([iter_combs[:, i] for i in range(k)])]
            assert np.all(new_combs == new_iter_combs)


def test_f90_perm_comb():
    for n in [2, 3, 4, 5]:
        for k in range(2, n+1, 1):
            n_combs = np.math.factorial(n) / np.math.factorial(k) / np.math.factorial(n - k)
            n_perms_per_comb = np.math.factorial(k)
            perms = cpf.calc_permcombs(n, k, n_perms_per_comb, n_combs).T
            new_perms = perms[np.lexsort([perms[:, i] for i in range(k)])]

            # Test against itertools, with n-pick-k: combinations then
            # permutations.
            iter_perms = np.array(list(itertools.permutations(np.arange(1, n+1, 1), r=k)))
            new_iter_perms = iter_perms[np.lexsort([iter_perms[:, i] for i in range(k)])]
            assert np.all(new_perms == new_iter_perms)


def test_factorial():
    for k in range(21):
        assert np.math.factorial(k) == cpf.factorial(k, k-1)
        assert np.math.factorial(k) == cpf.factorial(k, k)

    for k in range(21):
        assert cpf.factorial(k, 1) == k

    for k in range(21):
        for l in range(1, k+1):
            assert cpf.factorial(k, l) == np.math.factorial(k) / np.math.factorial(k - l)
