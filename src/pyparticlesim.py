#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Kamyar Modjtahedzadeh"

try:
    # If imported from ~/workspace
    from src.fields import *
    from src.particles_and_structures import *
    from src.verlet_simulation import *
except ImportError:
    # If imported from ~/workspace/src
    from fields import *
    from particles_and_structures import *
    from verlet_simulation import *
