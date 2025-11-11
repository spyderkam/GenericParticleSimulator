#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Gravitational collapse with time-varying repulsive force (breathing oscillations)

import matplotlib.pyplot as plt
import src.pyparticlesim.pyparticlesim as pps
import time

# Parameters
G = 10.0                    # Tested with grav_softening=0.05, dt=1e-5
grav_softening = 0.05       # Tested with G=10, dt=1e-5
k_zeta = 8.0                # Reduced from 15.0
zeta_softening = 0.05
zeta_amplitude = 0.5        # Reduced from 0.8
omega_zeta = 30.0           # Longer period, clearer oscillations (~1 cycle at t=0.08)
dt = 1e-5                   # Tested with G=10, grav_softening=0.05
n_steps = 4000

# Record start time
start_time = time.perf_counter()

# Create initial structure
struct = pps.Particle_Structure('circle', [0.0, 0.0, 1.0], 100)
initial_positions = [particle.pos.copy() for particle in struct.particles]

# Create field with gravity and time-varying repulsive force
field = pps.SK_Field(
    G=G, 
    grav_softening=grav_softening,
    k_zeta=k_zeta,
    zeta_softening=zeta_softening,
    zeta_amplitude=zeta_amplitude,
    omega_zeta=omega_zeta
)

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
plt.savefig(f'breathing_oscillations_verlet_{n_steps}.pdf', bbox_inches='tight')
plt.close()

elapsed_time = time.perf_counter() - start_time
print(f"Simulation runtime: {elapsed_time:.4f} seconds")
print(f"Final time: {sim.time:.3f}")
