import src.pyparticlesim as pps
import matplotlib.pyplot as plt
import numpy as np

part_rad = 1.0  # Particle radius

# Create particle structure
circle = pps.Particle_Structure('rectangle', [0.0, 0.0, 1.0, 1.0], 100, particle_radius=part_rad)
positions = [particle.pos for particle in circle.particles]

plt.plot([p[0] for p in positions], [p[1] for p in positions], 'bo', label='$t=0$')

# Create field
# ϵ (loosely) sets interaction strength and σ (= part_rad*2) should match particle diameter
field = pps.SK_Field(G=1)

# Run parameters
simulation_time = 0
dt = 0.01
n_steps = 100

# Run simulation
for _ in range(n_steps):
    forces = field.compute_forces(circle.particles)
    for i, particle in enumerate(circle.particles):
        particle.apply_forces(dt, forces[i])
    simulation_time += dt

# Check results
print(f"Final time: {simulation_time}")
#print(f"First particle position: {pps.ps.particles[0].pos}")

final_positions = [particle.pos for particle in circle.particles]

plt.plot([p[0] for p in final_positions], [p[1] for p in final_positions], 'r*', label=f'$t={n_steps*dt}$')
plt.axis('equal')
plt.legend()

plt.xlabel(r'$x$-axis', fontsize=15)
plt.ylabel(r'$y$-axis', fontsize=15)
plt.tight_layout()

plt.show()
plt.savefig('before_and_after.pdf', bbox_inches='tight')
plt.close()
