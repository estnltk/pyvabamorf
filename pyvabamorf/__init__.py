# -*- coding: utf-8 -*-
import pyvabamorf.vabamorf as vm
import atexit

if not vm.FSCInit():
    raise Exception('Could not initiate pyvabamorf library. FSCInit() returned false!')

@atexit.register
def terminate():
    vm.FSCTerminate()

from morf import analyze
from morf import PyVabamorf
