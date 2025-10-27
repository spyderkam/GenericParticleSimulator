from src.pyparticlesim import Particle_Structure, Simulation
import matplotlib.pyplot as plt
import numpy as np

# Before
ps = Particle_Structure('circle', [0, 0, 1.0], 10)
x0 = [p.pos[0] for p in ps.particles]
y0 = [p.pos[1] for p in ps.particles]

# Simulation run
sim = Simulation(ps.particles, dt=0.01)
def weight(p): return np.array([0.0, -9.81*p.mass])
sim.run(100, weight)

# After
x1 = [p.pos[0] for p in sim.particles]
y1 = [p.pos[1] for p in sim.particles]

# Plot
plt.plot(x0, y0, 'bo', label='$t=0$')
plt.legend()
plt.axis('equal')
#plt.savefig('before.pdf', bbox_inches='tight')

plt.plot(x1, y1, 'ro', label=r'$t = 1\,\mathrm{s}$')
plt.legend()
plt.axis('equal')

plt.savefig('before_after.pdf', bbox_inches='tight')
plt.close()
