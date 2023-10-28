************
Installation
************

Package Requirements
====================

Currently there are no strict criteria for installation; it is suggested that you use the most up-to-date package versions available. The one exception there is that the minimum version of Python is set to 3.8, and development is currently focused on Python 3.9+.

The current package requirements are:

* ``numpy``
* ``scipy``
* ``astropy``
* ``matplotlib``
* ``skypy``
* ``speclite``
* ``pandas``
* ``scikit-build-core``
* ``cmake``

with an optional dependency of

* ``mpi4py``.

For running the test suite the requirements are:

* ``tox``
* ``pytest``
* ``sphinx-fortran``
* ``sphinx-astropy``
* ``pytest-astropy``
* ``pytest-cov``.

Additionally, you will need the following to install ``macauff``:

* ``gfortran`` -- at least version 8
* ``git``

Installing the Package
======================

As of now, the only way to install this package is by downloading it from the `GitHub repository <https://github.com/Onoddil/macauff>`_. We recommend using an `Anaconda Distribution <https://www.anaconda.com/distribution/>`_, or `miniconda <https://docs.conda.io/en/latest/miniconda.html>`_, to maintain specific, independent Python installations without the need for root permissions.

Once you have installed your choice of conda, then you can create an initial conda environment::

    conda create -n your_environment_name -c conda-forge python=3.9 numpy scipy astropy matplotlib skypy speclite pandas scikit-build-core cmake

although you can drop the ``=3.9``, or chose another (later) Python version -- remembering the minimum version is 3.8 -- if you desire to do so. Then activate this as our Python environment::

    conda activate your_environment_name

If you require the additional test packages listed above, for running tests, you can install them separately with::

    conda install -c conda-forge tox pytest sphinx-astropy pytest-astropy pytest-cov
    conda install -c vacumm -c conda-forge sphinx-fortran

You will also need to install ``gfortran`` in order to compile the fortran code in this package. Instructions for how to install this for Windows, MacOS, or Linux can be found `here <https://gcc.gnu.org/wiki/GFortranBinaries>`_. Finally, install ``git`` if you do not have it on your computer; `instructions <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`_ for installing it on your operating system are available.

Once you have the required packages installed -- whether in a new ``conda`` environment or otherwise -- you can clone the repository::

    git clone git://github.com/onoddil/macauff.git

which will place the repository in the folder from which you invoked the ``git`` command. Now, from inside the folder that was just created (``cd macauff`` or equivalent), you can either run::

    pip install .

or::

    pip install . --config-settings=cmake.build-type="Debug"

which will install ``macauff`` such that you can ``import macauff`` from other folders on your computer. However, if this is to develop the software, your changes will not be reflected in the installed version of the code (and you must re-install using the above command); if you wish to have ``Python`` code changes immediately reflected in your ``pip``-installed version of the software, you can install ``macauff`` using::

    pip install -e .

or::

    pip install -e . --config-settings=cmake.build-type="Debug"

where ``-e`` is the "editable" flag. Note that the ``config-settings`` parameter passed through ``pip`` controls the optimisation flag for the compilation of Fortran code. With ``debug`` set, ``macauff`` will install with ``-O0`` optimisation and numerous additional check/debug flags, while by default the software will be installed with compiler optimisation.

To confirm your installation was successful, you can ``import macauff`` in a Python terminal.

OpenMP Setup
------------

Within the ``Fortran`` codebase, ``OpenMP`` is used in numerous places to parallelise independent operations. For these to work, several additional environment variables must be set.

First, ``OMP_NUM_THREADS`` must be set; in ``bash`` for example this would be ``export OMP_NUM_THREADS=10``. This should be set as high as reasonably possible to decrease overall runtime as much as possible.

Second, if large matches are likely to be used in the future, ``GOMP_STACKSIZE`` (and possibly ``OMP_STACKSIZE``, compiler dependent) should be increased. This should again be set as high as reasonably possible to avoid segmentation faults due to stack size.

Finally, again in the case of large catalogue runs, ``ulimit -s`` should be set to a higher number (in the limit ``ulimit -s unlimited`` can be used to remove the cap entirely) to avoid issues with overall stacksize.

Testing
=======

To run the main unit test suite, assuming you installed it during the above process, you can run::

    tox -e test

If you wish to locally build the documentation -- mostly likely if you are improving or extending the documentation, as the docs are available online -- you can run::

    tox -e build_docs


Getting Started
===============

Once you have installed the package, check out the :doc:`Quick Start<quickstart>` page.
