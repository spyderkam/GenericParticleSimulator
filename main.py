#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Gravitational collapse with velocity Verlet integration.

import matplotlib.pyplot as plt
import src.pyparticlesim as pps
import time

# Parameters
G = 10.0           # Reduced coupling
softening = 0.05   # Increased softening
dt = 1e-5          # Conservative timestep
n_steps = 10000    # Reaches t = 0.1

# Record start time
start_time = time.perf_counter()

# Create initial structure
struct = pps.Particle_Structure('circle', [0.0, 0.0, 1.0], 100)
initial_positions = [particle.pos.copy() for particle in struct.particles]

# Create gravitational field
field = pps.SK_Field(G=G, softening=softening)

# Initialize Verlet simulation
sim = pps.Verlet_Simulation(struct.particles, dt, field)

# Run simulation
sim.run(n_steps)

# Extract final positions
final_positions = [particle.pos for particle in sim.particles]

# Plot initial and final states
plt.plot([p[0] for p in initial_positions], [p[1] for p in initial_positions], 'bo', label='$t=0$')
plt.plot([p[0] for p in final_positions], [p[1] for p in final_positions], 'r*', label=f'$t={sim.time:.3f}$')

# Plot settings
plt.grid(True)
plt.axis('equal')
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.xlabel(r'$x$-axis', fontsize=15)
plt.ylabel(r'$y$-axis', fontsize=15)
plt.legend()
plt.tight_layout()

# Save and report runtime
plt.savefig('gravitational_collapse_verlet.pdf', bbox_inches='tight')
plt.close()

elapsed_time = time.perf_counter() - start_time
print(f"Simulation runtime: {elapsed_time:.4f} seconds")
print(f"Final time: {sim.time:.3f}")
