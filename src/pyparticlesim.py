#!/usr/bin/env python3

import numpy as np

class Particle:
    """
    2D particle for general simulation framework.
    
    Force accumulator (fx, fy) allows independent force computations 
    to be summed before updating motion.
    """
    
    def __init__(self, position, velocity=(0.0, 0.0), mass=1.0, radius=1.0):
        """
        Args:
            position : [x, y] array-like
            velocity : [vx, vy] array-like (default: [0, 0])
            mass     : particle mass (default: 1.0)
            radius   : particle radius (default: 1.0)
        """
        
        self.pos = np.array(position, dtype=float)   # [x, y]
        self.vel = np.array(velocity, dtype=float)   # [vx, vy]
        self.mass = mass
        self.radius = radius
        self.force = np.array([0.0, 0.0])            # [fx, fy] accumulator

    def advance(self, dt, method='euler'):
        """Update position and velocity using accumulated forces."""
        if method == 'euler':
            self._advance_euler(dt)
        elif method == 'verlet':
            self._advance_verlet(dt)
            # For Verlet, we'll need to store self.accel_prev (previous acceleration).
            # We must add that attribute to __init__ and initialize it to zero.
        else:
            raise ValueError(f"Unknown integration method: {method}")
    
    def _advance_euler(self, dt):
        acceleration = self.force / self.mass
        self.vel += acceleration * dt
        self.pos += self.vel * dt
