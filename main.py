from src.pyparticlesim import Particle, Particle_Structure, Simulation
import matplotlib.pyplot as plt
import numpy as np

struct = Particle_Structure(structure='rectangle', init_points=[0, 0, 2.0, 1.0], nParticles=50)
positions_0 = [particle.pos for particle in struct.particles]

def weight(particle):
    if not isinstance(particle, Particle):
        raise ValueError("Input must be a Particle object")
    return np.array([0.0, -9.81*particle.mass])

plt.plot([p[0] for p in positions_0], [p[1] for p in positions_0], 'bo', label='$t=0$')
plt.savefig('initial.pdf', bbox_inches='tight')
plt.close()

part0 = Particle(position=[0.0, 0.0], velocity=[5.0, 10.0], mass=1.0, radius=1.0)
part1 = Particle(position=[2.0, 1.0], velocity=[20.0, 1.0], mass=1.0, radius=1.0)


#print( (np.linalg.norm(part0.vel)*np.linalg.norm(part1.vel))/(np.linalg.norm(part0.pos - part1.pos)**2) )

def generic_central_force(particle1: Particle, particle2: Particle, k=1.0):
    """$$\pm k \frac{\left\vert v_1v_2\right\vert}{r^2} \hat{r}$$"""

    if not isinstance(particle1, Particle) and not isinstance(particle2, Particle):
         raise ValueError("At least one of the particles is NOT an instance of the Particle class")

    distance_vector = particle1.pos - particle2.pos
    distance = np.linalg.norm(distance_vector)
    velocity_product = np.linalg.norm(particle1.vel)*np.linalg.norm(particle2.vel)

    central_force = (k*velocity_product/distance**3)*distance_vector
    return central_force

print(generic_central_force(part0, part1))