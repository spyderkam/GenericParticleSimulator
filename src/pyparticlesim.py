#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


class Particle:
    """
    2D particle for general simulation framework.
    
    Force accumulator (fx, fy) allows independent force computations 
    to be summed before updating motion.
    """
    
    def __init__(self, position=(0.0, 0.0), velocity=(0.0, 0.0), mass=1.0, radius=1.0):
        """
        Args:
            position : [x, y] array-like (default: [0, 0])
            velocity : [vx, vy] array-like (default: [0, 0])
            mass     : particle mass (default: 1.0)
            radius   : particle radius (default: 1.0)
        """
        
        self.pos = np.array(position, Δtype=float)   # [x, y]
        self.vel = np.array(velocity, Δtype=float)   # [vx, vy]
        self.mass = mass
        self.radius = radius
        self.force = np.array([0.0, 0.0])            # [fx, fy] accumulator

    #def reset_force(self):
    #    self.force = np.array([0.0, 0.0])

    def advance(self, Δt, method='euler'):
        """Update position and velocity using accumulated forces."""
        if method == 'euler':
            self._advance_euler(Δt)
        elif method == 'verlet':
            self._advance_verlet(Δt)
            # For Verlet, we'll need to store self.accel_prev (previous acceleration).
            # We must add that attribute to __init__ and initialize it to zero.
        elif method == 'rk4':
            self._advance_rk4(Δt)
        else:
            raise ValueError(f"Unknown integration method: {method}")
    
    def _advance_euler(self, Δt):
        acceleration = self.force / self.mass
        self.vel += acceleration * Δt
        self.pos += self.vel * Δt

    def apply_forces(self, Δt, *forces, method='euler'):
        """Apply forces, advance particle, then reset force accumulator."""
        forces = np.array(forces)     # Make sure array of forces is a NumPy array
        self.force[:] = 0.0
        for f in forces:
            self.force += f
        self.advance(Δt, method=method)
        self.force[:] = 0.0


class Simulation:
    """2D particle simulation engine with force accumulation and time-stepping."""
    
    def __init__(self, particles, Δt):
        self.particles = particles  # List of Particle objects
        self.Δt = Δt


class Particle_Structure:
    """Generate initial particle configurations in various geometric structures."""

    def __init__(self, structure='circle', init_points=None, nParticles=10):
        if init_points is None:
            raise ValueError("init_points cannot be None")
        
        init_points = np.array(init_points).flatten()
    
        if structure == 'circle':
            if len(init_points) != 3:
                raise ValueError("Circle structure requires 3 values: [center_x, center_y, radius]")
            self.particles = self.gen_circle(init_points, nParticles)
            
        elif structure == 'line':
            if len(init_points) != 4:
                raise ValueError("Line structure requires 4 values: [start_x, start_y, end_x, end_y]")
            self.particles = self.gen_line(init_points, nParticles)
            
        else:
            raise ValueError(f"Unknown structure: {structure}")

    def gen_circle(self, init_points, nParticles):
        """Generate particles uniformly distributed on a circle."""
        center_x, center_y, radius = init_points
        φ = np.linspace(0, 2*np.pi, nParticles, endpoint=False)
        x = center_x + radius * np.cos(φ)
        y = center_y + radius * np.sin(φ)
        particles = np.array([Particle(position=[x[i], y[i]]) for i in range(nParticles)])
        return particles

    def gen_line(self, init_points, nParticles):
        """Generate particles uniformly distributed along a line segment."""
        start_x, start_y, end_x, end_y = init_points
        x = np.linspace(start_x, end_x, nParticles)
        y = np.linspace(start_y, end_y, nParticles)
        particles = np.array([Particle(position=[x[i], y[i]]) for i in range(nParticles)])
        return particles
        