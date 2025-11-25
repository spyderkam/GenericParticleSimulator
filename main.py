#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import src.pyparticlesim as pps

# Fixed parameters
G = 10.0
grav_softening = 0.05
omega_zeta = 300
dt = 1e-5
n_steps = 8000  # c ≈ 4
n_particles = 100

# Scan parameters
lambda_values = [0.844]

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
    R_avg = np.mean(radii)
    R_std = np.std(radii)
    
    results.append({
        'lambda': lambda_,
        'R_avg': R_avg,
        'R_std': R_std,
    })
    
    print(f"λ={lambda_:.3f}: R_avg={R_avg:.3f}, R_std={R_std:.3f}")

# Save results
#np.save('./data/lambda_scan_2cycles_n4000/lambda_scan_results.npy', results)
