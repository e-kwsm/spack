# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Ntchem(CMakePackage):
    """NTChem is a high-performance software package for the molecular
    electronic structure calculation for general purpose on the K computer. It
    is a comprehensive new software of ab initio quantum chemistry made in
    R-CCS (former AICS) from scratch. NTChem contains not only standard quantum
    chemistry approaches but our own original approaches. NTChem is expected to
    be a useful tool in various computational studies for large and complicated
    molecular systems.
    """

    homepage = 'https://molsc.riken.jp/index.html'
    git = 'https://gitlab.com/ntqc/ntchem2013.git'
    maintainers = ['e-kwsm']

    version('master', branch='master')
    version('11.0', tag='11.0')
    version('10.0', tag='10.0')

    variant('parallel', default='mpiomp', description='Parallelization',
            values=('serial', 'mpi', 'mpiomp'))

    depends_on('blas', type='link')
    depends_on('cmake@3.7:', type='build')
    depends_on('fftw@3: -mpi -openmp', type='link', when='parallel=serial')
    depends_on('fftw@3: +mpi -openmp', type='link', when='parallel=mpi')
    depends_on('fftw@3: +mpi +openmp', type='link', when='parallel=mpiomp')
    depends_on('lapack', type='link')
    depends_on('mpi', type=('build', 'link'), when='parallel=serial')
    depends_on('mpi', type=('build', 'link', 'run'), when='parallel=mpi')
    depends_on('mpi', type=('build', 'link', 'run'), when='parallel=mpiomp')

    def cmake_args(self):
        args = [
            '-DCMAKE_C_COMPILER={0}'.format(self.spec['mpi'].mpicc),
            '-DCMAKE_CXX_COMPILER={0}'.format(self.spec['mpi'].mpicxx),
            '-DCMAKE_Fortran_COMPILER={0}'.format(self.spec['mpi'].mpifc),
            '-DPARALLEL={0}'.format(self.spec.variants['parallel'].value)
        ]
        return args
