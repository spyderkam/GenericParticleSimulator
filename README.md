# PyParticleSim

A general-purpose 2D particle simulation framework written in Python.

**Current Version:** v0.1.0

## Overview

PyParticleSim provides a modular, extensible framework for simulating systems of many particles. The architecture is designed to handle diverse physics domains including molecular dynamics, debris cloud propagation, n-body gravitational systems, and more.

## Features

- **Generalized Particle Class**: Base particle representation with position, velocity, mass, and radius
- **Force Accumulator Pattern**: Clean separation of force calculations from integration
- **Euler Integration**: Time-stepping with Euler method (Verlet and RK4 support planned)
- **Particle Structure Generator**: Create initial configurations (line, circle, rectangle)
- **Simulation Engine**: Time-stepping loop with `step()` and `run()` methods
- **NumPy-based**: Efficient numerical computations
- **Modular Design**: Easy to extend with new force models and integrators

## Core Components

- `Particle`: Base 2D particle class with force accumulator
- `Simulation`: Time-stepping engine for advancing particle systems
- `Particle_Structure`: Geometric initialization (line, circle, rectangle)
- `ForceField`: Pluggable physics models (coming soon)

## Requirements

- Python 3.11+
- NumPy

## Installation
```bash
pip install numpy
```

## Usage

### Basic Particle
```python
from src.pyparticlesim import Particle
import numpy as np

# Create and advance a single particle
p = Particle(position=[0.0, 0.0], velocity=[1.0, 1.0], mass=1.0)
f_gravity = np.array([0.0, -9.8])
f_wind = np.array([1.0, 0.0])
p.apply_forces(dt=0.1, f_gravity, f_wind)
print(p.pos, p.vel)
```

### Particle Structure
```python
from src.pyparticlesim import Particle_Structure

# Line of 10 particles
line = Particle_Structure('line', init_points=[0, 0, 1, 1], nParticles=10)

# Circle of 20 particles
circle = Particle_Structure('circle', init_points=[0, 0, 1.5], nParticles=20)

# Rectangle of 16 particles
rect = Particle_Structure('rectangle', init_points=[0, 0, 2, 1], nParticles=16)
```

### Simulation
```python
from src.pyparticlesim import Simulation

# Create particle structure
ps = Particle_Structure('circle', [0, 0, 1.0], 10)

# Initialize and run simulation
sim = Simulation(ps.particles, Δt=0.01)
f = np.array([0.0, -9.8])  # Apply gravity
sim.run(100, f)  # Run for 100 timesteps

# Check final positions
for particle in sim.particles:
    print(particle.pos)
```

### User-Defined Force Functions

Define force functions that return `[Fx, Fy]` arrays:

```python
def gravity(particle: Particle) -> np.ndarray:
    """Gravitational force (no parameters needed)."""
    return np.array([0.0, -9.81 * particle.mass])

def drag(particle: Particle, b: float) -> np.ndarray:
    """Velocity-dependent drag force."""
    return -b * particle.vel

def spring(particle: Particle, anchor: np.ndarray, k: float, L0: float) -> np.ndarray:
    """Spring force toward anchor point with rest length L0."""
    delta = particle.pos - anchor
    r = np.linalg.norm(delta)
    if r == 0:
        return np.array([0.0, 0.0])
    return -k * (r - L0) * (delta / r)

# Apply multiple forces
for particle in sim.particles:
    particle.apply_forces(
        dt=0.01,
        gravity(particle),
        drag(particle, b=0.5),
        spring(particle, np.array([0, 0]), k=10.0, L0=1.0)
    )
```

## Project Status

🚧 **v0.1.0** - Active development

**Implemented:**
- Particle class with Euler integration
- Force accumulator pattern
- Simulation time-stepping engine
- Geometric structure generators (line, circle, rectangle)

**Planned:**
- Verlet and RK4 integrators
- Force field classes (gravity, springs, drag, collisions)
- Boundary conditions
- Energy/momentum diagnostics
- Visualization utilities

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/spyderkam/GenericParticleSimulator/blob/main/LICENSE) file for details.
