from distutils.core import setup, Extension
import os

def get_sources(src_dir='src', ending='.cpp'):
    '''Function to get a list of files ending with `ending` in `src_dir`.'''
    return [os.path.join(src_dir, fnm) for fnm in os.listdir(src_dir) if fnm.endswith(ending)]

# define directories for vabamorf source directories
dirs = ['fsc', 'proof', 'etana', 'json']
src_dirs = [os.path.join('src', d) for d in dirs]

# define a list of C++ source files
lib_sources = []
for d in src_dirs:
    lib_sources.extend(get_sources(d))

# define directories for vabamorf include directories
dirs.append(os.path.join('fsc', 'fsjni'))
include_dirs = [os.path.join('include', d) for d in dirs]

# define the vabamorf SWIG wrapper generator interface file
swig_interface = os.path.join('pyvabamorf', 'vabamorf.i')

setup(name='pyvabamorf',
    version="1.0",
    description='Python interface for the Vabamorf Estonian lemmatizer and morphological analyzer.',
    author='Tarmo Vaino, Heiki-Jaan Kaalep, Sven Laur, Timo Petmanson, Aleksandr Tkachenko, Siim Orasmaa',
    author_email='tpetmanson@gmail.com',
    url='https://github.com/brainscauseminds/pyvabamorf',

    ext_modules = [
        Extension('_vabamorf',
                  [swig_interface] + lib_sources,
                  swig_opts = ['-c++'],
                  include_dirs=include_dirs)
        ],
    packages = ['pyvabamorf'],
    package_dir = {'pyvabamorf': 'pyvabamorf'},
    package_data = {'pyvabamorf': [os.path.join('dct', 'et.dct')]}
    )
