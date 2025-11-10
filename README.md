# PyParticleSim

A general-purpose 2D particle simulation framework written in Python.

**Current Version:** v0.2.0

## Overview

PyParticleSim provides a modular, extensible framework for simulating systems of many particles. The architecture is designed to handle diverse physics domains including molecular dynamics, debris cloud propagation, N-body gravitational systems, and more.

## Features

- **Generalized Particle Class**: Base particle representation with position, velocity, mass, and radius
- **Force Accumulator Pattern**: Clean separation of force calculations from integration
- **Multiple Integration Methods**: Standard Euler and Velocity Verlet (symplectic)
- **Particle Structure Generator**: Create initial configurations (line, circle, rectangle, diamond, solid shapes)
- **N-body Force Fields**: Gravitational and repulsive interactions with softening
- **Simulation Engines**: User-defined forces and field-based dynamics
- **NumPy-based**: Efficient numerical computations
- **Modular Design**: Easy to extend with new force models and integrators

## Core Components

- `Particle`: Base 2D particle class with force accumulator
- `User_Simulation`: Time-stepping engine for user-defined forces
- `Verlet_Simulation`: Velocity Verlet integration for conservative systems
- `SK_Field`: N-body force field (gravity, Lennard-Jones)
- `Particle_Structure`: Geometric initialization with multiple shapes

## Project Structure

```
workspace/
├── src/
│   ├── int_euler.py                     # Integration script examples
│   ├── int_verlet.py
│   └── pyparticlesim/
│       ├── particles_and_structures.py  # Particle, User_Simulation, Particle_Structure
│       ├── fields.py                    # SK_Field
│       ├── verlet_simulation.py         # Verlet_Simulation
│       └── pyparticlesim.py             # Main module (imports all)
```

**Note:** Package initialization (`__init__.py`) will be implemented in future versions for cleaner imports.

## Usage

### Particle Structure Generation

```python
from src.pyparticlesim.particles_and_structures import Particle_Structure

# Circle of 20 particles
circle = Particle_Structure('circle', init_points=[0, 0, 1.5], nParticles=20)
```

Available structures: `'circle'`, `'line'`, `'rectangle'`, `'diamond'`, `'solid_circle'`, `'solid_diamond'`

### User-Defined Force Simulation

```python
from src.pyparticlesim.particles_and_structures import Particle_Structure, User_Simulation
import numpy as np

# Define force functions
def weight(particle):
    """Gravitational weight force."""
    return np.array([0.0, -9.81 * particle.mass])

def drag(particle, b=0.5):
    """Velocity-dependent drag force."""
    return -b * particle.vel

def spring(particle, anchor, k=10.0, L0=1.0):
    """Spring force toward anchor point."""
    delta = particle.pos - anchor
    r = np.linalg.norm(delta)
    if r == 0:
        return np.array([0.0, 0.0])
    return -k * (r - L0) * (delta / r)

# Create simulation
ps = Particle_Structure('circle', [0, 0, 1.0], 10)
sim = User_Simulation(ps.particles, dt=0.01)

# Run with multiple forces
anchor = np.array([0, 0])
sim.run(100, weight, lambda p: drag(p, 0.5), lambda p: spring(p, anchor, 10.0, 1.0))
```

### N-body Gravitational Simulation

```python
from src.pyparticlesim.particles_and_structures import Particle_Structure
from src.pyparticlesim.fields import SK_Field
from src.pyparticlesim.verlet_simulation import Verlet_Simulation

# Create particle structure
square = Particle_Structure('rectangle', [0.0, 0.0, 1.0, 1.0], 100)

# Create gravitational field with softening
field = SK_Field(G=100.0, grav_softening=0.05)

# Initialize Velocity Verlet simulation
sim = Verlet_Simulation(square.particles, dt=1e-5, field=field)

# Run simulation
sim.run(10000)

# Access final state
print(f"Final time: {sim.time}")
for particle in sim.particles:
    print(particle.pos, particle.vel)
```

### Combined Force Fields

```python
from src.pyparticlesim.fields import SK_Field

# Gravitational and repulsive forces (balances collapse)
field = SK_Field(G=10.0, grav_softening=0.01, k_repulsive=1.0, repulsive_softening=0.01)
```

## Integration Methods

### Standard Euler (1st-order)
- Simple, fast
- Energy drift over time
- Use for: short simulations, non-conservative systems

### Velocity Verlet (2nd-order, symplectic)
- Bounded energy errors
- Phase space preservation
- Time-reversible
- Use for: long simulations, conservative systems, energy conservation critical
- Note: ~2× computational cost (two force evaluations per step)

## Project Status

**v0.2.0** - Active development

**Implemented:**
- Particle class with standard Euler integration
- Force accumulator pattern
- User_Simulation for custom forces
- Verlet_Simulation for symplectic integration
- SK_Field for N-body interactions (gravity, repulsive force)
- Geometric structure generators (6 types including solid shapes)
- Softening parameters for gravitational and repulsive force singularity prevention

**Planned:**
- Trajectory recording system
- Animation tools
- Energy/momentum diagnostics
- Additional force fields (Coulomb, Yukawa)
- Boundary conditions
- Collision detection
- Spatial partitioning optimization

## Academic Paper

This framework supports ongoing research documented in:

**"Numerical Instability in Gravitational N-Body Simulations: A Comparative Analysis"**

Key findings:
- Euler method exhibits catastrophic energy injection when timesteps are too large
- Velocity Verlet maintains bounded energy errors through symplectic structure
- For strongly coupled systems (G ≥ 50), timestep constraints apply regardless of method
- At long timescales (t=0.1), Verlet preserves orbital structure while Euler produces chaotic collapse

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/spyderkam/GenericParticleSimulator/blob/main/LICENSE) file for details.

## Author

Kamyar Modjtahedzadeh  
Portfolio: [spyderkam.com](https://spyderkam.com)
