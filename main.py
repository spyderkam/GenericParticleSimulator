import src.pyparticlesim as pps
import matplotlib.pyplot as plt
import numpy as np

part_rad = 1.0  # Particle radius

# Create particle structure
circle = pps.Particle_Structure('solid_circle', [0.0, 0.0, 1.0], 1000, particle_radius=part_rad)
positions = [particle.pos for particle in circle.particles]

plt.plot([p[0] for p in positions], [p[1] for p in positions], 'bo', label='$t=0$')
plt.axis('equal')
plt.tight_layout()
#plt.show()
plt.savefig('init_struct.pdf', bbox_inches='tight')
plt.close()

# Create field
# ϵ (loosely) sets interaction strength and σ should match particle diameter
field = pps.SK_Field(epsilon=10000.0, sigma=part_rad*2)

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

plt.plot([p[0] for p in final_positions], [p[1] for p in final_positions], 'bo', label='$t=0$')
plt.axis('equal')
plt.tight_layout()
plt.show()
plt.savefig('last_struc.pdf', bbox_inches='tight')
plt.close()
