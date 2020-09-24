from spack import *


class Rdkit(CMakePackage):
    """RDKit is a collection of cheminformatics and machine-learning software
    written in C++ and Python.
    """
    homepage = 'https://www.rdkit.org/docs/index.html'
    git = 'https://github.com/rdkit/rdkit.git'

    version('master', branch='master')
    version('2020_03_5', tag='Release_2020_03_5')
    version('2020_03_4', tag='Release_2020_03_4')
    version('2020_03_3', tag='Release_2020_03_3')
    version('2020_03_2', tag='Release_2020_03_2')
    version('2020_03_1', tag='Release_2020_03_1')
    version('2019_09_3', tag='Release_2019_09_3')
    version('2019_09_2', tag='Release_2019_09_2')
    version('2019_09_1', tag='Release_2019_09_1')
    version('2019_03_4', tag='Release_2019_03_4')
    version('2019_03_3', tag='Release_2019_03_3')
    version('2019_03_2', tag='Release_2019_03_2')
    version('2019_03_1', tag='Release_2019_03_1')

    variant('eigen', default=True, description='Enable Eigen binding')
    variant('postgresql', default=False, description='Build the PostgreSQL cartridge')
    variant('python', default=True, description='Build the standard python wrappers')
    variant('swig', default=False, description='Build the SWIG wrappers')

    depends_on('boost @1.56.0:'
        ' +iostreams'
        ' +program_options'
        ' +python'
        ' +regex'
        ' +serialization'
        ' +system'
    )
    depends_on('cairo')
    depends_on('cmake', type='build')
    depends_on('eigen', when='+eigen')
    depends_on('postgresql', when='+postgresql')
    depends_on('python@3:', type=('build', 'link', 'run'), when='+python')
    depends_on('swig', when='+java +swig')

    def cmake_args(self):
        args = []
        if 'python' in self.spec:
            args = +[
                '-DCMAKE_INSTALL_PREFIX={0}'.format(self.spec.prefix),
                '-DPYTHON_EXECUTABLE={0}'.format(self.spec['python'].command.path),
                '-DRDK_INSTALL_INTREE=NO',
            ]
        return args
