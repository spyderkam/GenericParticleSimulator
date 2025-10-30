from src.pyparticlesim import Particle, Particle_Structure, Simulation
import matplotlib.pyplot as plt
import numpy as np

def weight(particle):
    if not isinstance(particle, Particle):
        raise ValueError("Input must be a Particle object")
    return np.array([0.0, -9.81*particle.mass])

def generic_central_force(particle1: Particle, particle2: Particle, k=1.0):
    """$$\pm k \frac{\left\vert v_1v_2\right\vert}{r^2} \hat{r}$$"""

    if not isinstance(particle1, Particle) and not isinstance(particle2, Particle):
         raise ValueError("At least one of the particles is NOT an instance of the Particle class")

    distance_vector = particle1.pos - particle2.pos
    distance = np.linalg.norm(distance_vector)
    velocity_product = np.linalg.norm(particle1.vel)*np.linalg.norm(particle2.vel)

    central_force = (k*velocity_product/distance**3)*distance_vector
    return central_force

# ***

circle = Particle_Structure('solid_circle', init_points=[0.0, 0.0, 1.0], nParticles=1200)
positions = [particle.pos for particle in circle.particles]

plt.plot([p[0] for p in positions], [p[1] for p in positions], 'bo', label='$t=0$')
plt.axis('equal')
plt.tight_layout()
#plt.show()
plt.savefig('solid_circle.pdf', bbox_inches='tight')
#plt.close()
