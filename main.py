from src.pyparticlesim import *

# Example usage

print("\nBasic Example:")
p = Particle(position=[0.0, 0.0], velocity=[1.0, 1.0], mass=1.0, radius=1.0)
print(p.pos, p.vel)
f1 = np.array([0.0, -9.8])  # Gravity
f2 = np.array([1.0, 0.0])   # Constant force
f = np.sum([f1, f2], axis=0)
dt = 0.1
p.apply_forces(dt, f1, f2)  # f vs. f1, f2
print(p.pos, p.vel)

print("\nParticle Structure Example:")
part_struct = Particle_Structure(structure='circle', init_points=[0.0, 0.0, 1.0], nParticles=10)
particles = part_struct.particles
for particle in particles:
    print(particle.pos)