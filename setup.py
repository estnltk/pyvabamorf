# -*- coding: utf-8 -*-
from setuptools import setup, find_packages, Extension
import os
import sys

os.environ['CC'] = 'g++'
os.environ['CXX'] = 'g++'

def get_sources(src_dir='src', ending='.cpp'):
    """Function to get a list of files ending with `ending` in `src_dir`."""
    return [os.path.join(src_dir, fnm) for fnm in os.listdir(src_dir) if fnm.endswith(ending)]

# define directories for vabamorf source directories
dirs = ['etana', 'etyhh', 'fsc', 'json', 'proof']
src_dirs = [os.path.join('src', d) for d in dirs]

# define a list of C++ source files
lib_sources = []
vabamorf_src = os.path.join('src', 'etana', 'vabamorf.cpp')
for d in src_dirs:
    lib_sources.extend(get_sources(d))
lib_sources.remove(vabamorf_src) # we add it later as the first file to compile
                                 # less time to wait, when working with vabamorf wrapper

# define directories for vabamorf include directories
dirs.append(os.path.join('fsc', 'fsjni'))
include_dirs = [os.path.join('include', d) for d in dirs]

# define the vabamorf SWIG wrapper generator interface file
swig_interface = os.path.join('pyvabamorf', 'vabamorf.i')
swig_opts = ['-builtin']

# Python 3 specific configuration
extra = {}
if sys.version_info[0] == 3:
    swig_opts.append('-py3')
swig_opts.append('-c++')


setup(name='pyvabamorf',
    version="1.7",
    description='Python interface for the Vabamorf Estonian lemmatizer and morphological analyzer.',
    author='Tarmo Vaino, Heiki-Jaan Kaalep, Sven Laur, Timo Petmanson, Aleksandr Tkachenko, Siim Orasmaa, Raul Sirel',
    author_email='tpetmanson@gmail.com',
    url='https://github.com/brainscauseminds/pyvabamorf',
    classifiers = ['Intended Audience :: Developers',
                   'Intended Audience :: Education',
                   'Intended Audience :: Science/Research',
                   'Intended Audience :: Information Technology',
                   'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                   'Operating System :: OS Independent',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Scientific/Engineering :: Artificial Intelligence',
                   'Topic :: Scientific/Engineering :: Information Analysis',
                   'Topic :: Text Processing',
                   'Topic :: Text Processing :: Linguistic'],

    ext_modules = [
        Extension('estnltk.vabamorf._vabamorf',
                  [swig_interface, vabamorf_src] + lib_sources,
                  swig_opts = swig_opts,
                  include_dirs=include_dirs)
        ],

    packages = find_packages(),
    include_package_data=True,
    package_data = {
        'pyvabamorf': ['dct/*.dct'],
    },
    )
