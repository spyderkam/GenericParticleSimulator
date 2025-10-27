
> For now, I will not be developing the `PyParticleSim` package. I will be testing what i have, the code seems to be working but I need to see the physics of outputs.

Good plan. For visualization, you'll want:

**Quick test - matplotlib:**
```python
import matplotlib.pyplot as plt

# After sim.run()
x = [p.pos[0] for p in sim.particles]
y = [p.pos[1] for p in sim.particles]
plt.scatter(x, y)
plt.axis('equal')
plt.show()
```

**Animation - track positions over time:**
Store positions at each timestep in `Simulation.run()` for trajectory plots.
