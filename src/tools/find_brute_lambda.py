#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import src.pyparticlesim as pps

def nsteps_from_cycles(cycles: float, dt: float = 1e-5, omega_zeta: float = 300) -> int:
    """Compute number of steps for given number of cycles."""
    return int(cycles*2*np.pi/(omega_zeta*dt))

# Steps and cycles
cycles = 4
n_steps = 8000  # c ≈ 4

# Fixed parameters
G = 10.0
grav_softening = 0.05
omega_zeta = 300
dt = 1e-5
n_particles = 100

# Scan parameters
lambda_values = np.linspace(0.8, 0.9, 10)

results = []

for lambda_ in lambda_values:
    # Create ring
    struct = pps.Particle_Structure('circle', [0.0, 0.0, 1.0], n_particles)
    
    # Create field
    field = pps.SK_Field(
        G=G,
        grav_softening=grav_softening,
        omega_zeta=omega_zeta,
        k_zeta=lambda_*G,
        zeta_softening=grav_softening,
    )
    
    # Run simulation
    sim = pps.Verlet_Simulation(struct.particles, dt, field)
    sim.run(n_steps)
    
    # Compute diagnostics
    radii = [np.linalg.norm(p.pos) for p in sim.particles]
    R_ave = np.mean(radii)
    R_std = np.std(radii)
    
    results.append((
        lambda_,
        R_ave,
        R_std,
    ))
    
    print(f"λ={lambda_:.6f}: R_ave={R_avg:.6f}, R_std={R_std:.6f}")

# Brute force search for optimal lambda. Not continued...
