# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function, absolute_import

from . import vabamorf as vm
from .morf import Vabamorf, analyze, synthesize, spellcheck
import atexit

if not vm.FSCInit():
    raise Exception('Could not initiate pyvabamorf library. FSCInit() returned false!')

@atexit.register
def terminate():
    vm.FSCTerminate()
