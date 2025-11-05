#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Kamyar Modjtahedzadeh"

try:
    # If imported from ~/workspace
    from src.pyparticlesim.fields import *
    from src.pyparticlesim.particles_and_structures import *
    from src.pyparticlesim.verlet_simulation import *
except ImportError:
    # If imported from ~/workspace/src
    from pyparticlesim.fields import *
    from pyparticlesim.particles_and_structures import *
    from pyparticlesim.verlet_simulation import *
except ImportError:
    # If imported from ~/workspace/src/pyparticlesim
    from fields import *
    from particles_and_structures import *
    from verlet_simulation import *
