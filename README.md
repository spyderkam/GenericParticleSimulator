# ParticleSim

A general-purpose 2D particle simulation framework written in Python.

## Overview

ParticleSim provides a modular, extensible framework for simulating systems of many particles. The architecture is designed to handle diverse physics domains including molecular dynamics, debris cloud propagation, n-body gravitational systems, and more.

## Features

- **Generalized Particle Class**: Base particle representation with position, velocity, mass, and radius
- **Force Accumulator Pattern**: Clean separation of force calculations from integration
- **NumPy-based**: Efficient numerical computations
- **Modular Design**: Easy to extend with new force models and integrators

## Core Components

- `Particle`: Base 2D particle class
- `Simulation`: Simulation engine (coming soon)
- `ForceField`: Pluggable physics models (coming soon)
- `Integrator`: Time-stepping algorithms (coming soon)

## Requirements

- Python 3.11+
- NumPy

## Installation
```bash
pip install numpy
```

## Usage
```python
from particle import Particle

# Create a particle at position (1.0, 2.0)
p = Particle(position=[1.0, 2.0], mass=2.5, radius=0.5)
```

## Project Status

🚧 In active development

