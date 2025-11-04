#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Gravitational collapse with Euler integration.

import src.pyparticlesim as pps
import matplotlib.pyplot as plt
import numpy as np
import time

part_rad = 1.0  # Particle radius (no usage outside of σ = part_rad*2 yet)

# Record the script start time
start_time = time.perf_counter()

# Create particle structure
struct = pps.Particle_Structure('rectangle', [0.0, 0.0, 1.0, 1.0], 100, particle_radius=part_rad)
positions = [particle.pos for particle in struct.particles]

plt.plot([p[0] for p in positions], [p[1] for p in positions], 'bo', label='$t=0$')

# Run parameters
simulation_time = 0
G = 10.0           # Reduced coupling
softening = 0.05   # Increased softening
dt = 1e-5          # Conservative timestep
n_steps = 10000    # Reaches t = 0.1

# Create field
# ϵ (loosely) sets interaction strength and σ should match particle diameter
field = pps.SK_Field(G=100, softening=softening)

# Run simulation
for _ in range(n_steps):
    forces = field.compute_forces(struct.particles)
    for i, particle in enumerate(struct.particles):
        particle.apply_forces(dt, forces[i])
    simulation_time += dt

final_positions = [particle.pos for particle in struct.particles]

plt.plot([p[0] for p in final_positions], [p[1] for p in final_positions], 'r*', label=f'$t={n_steps*dt}$')

# Plot settings
plt.grid(True)
plt.axis('equal')
plt.xlim(-0.5, 1.5)
plt.ylim(-0.5, 1.5)
plt.xlabel(r'$x$-axis', fontsize=15)
plt.ylabel(r'$y$-axis', fontsize=15)
plt.legend()
plt.tight_layout()

# Record the script end time
end_time = time.perf_counter()
# Calculate the script duration and print
elapsed_time = end_time - start_time
print(f"Simulation runtime: {elapsed_time:.4f} seconds")

#plt.show()
plt.savefig('gravitational_collapse_euler.pdf', bbox_inches='tight')
plt.close()
