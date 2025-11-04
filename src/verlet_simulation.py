#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Kamyar Modjtahedzadeh"

import numpy as np


class Verlet_Simulation:
    """
    Velocity Verlet simulation engine with proper force re-evaluation.
    
    Implements 2nd-order symplectic integration by recomputing forces
    after position update. Compatible with SK_Field.compute_forces().
    """
    
    def __init__(self, particles, dt, field):
        """
        Args:
            particles: Array of Particle objects
            dt: Timestep
            field: SK_Field instance for force computation
        """
        self.particles = np.array(particles)
        self.dt = dt
        self.field = field
        self.time = 0.0
    
    def step(self):
        """
        Single velocity Verlet timestep.
        
        Algorithm:
            1. Store a(t) = F(t)/m
            2. Update r(t+Δt) = r(t) + v(t)Δt + (1/2)a(t)Δt²
            3. Recompute F(t+Δt) from new positions
            4. Compute a(t+Δt) = F(t+Δt)/m
            5. Update v(t+Δt) = v(t) + (1/2)[a(t) + a(t+Δt)]Δt
        """
        n = len(self.particles)
        
        # Step 1: Compute and store current accelerations
        forces_old = self.field.compute_forces(self.particles)
        accel_old = np.array([forces_old[i] / self.particles[i].mass 
                              for i in range(n)])
        
        # Step 2: Update positions
        for i, particle in enumerate(self.particles):
            particle.pos += particle.vel * self.dt + 0.5 * accel_old[i] * self.dt**2
        
        # Step 3: Recompute forces at new positions
        forces_new = self.field.compute_forces(self.particles)
        
        # Steps 4-5: Update velocities with averaged acceleration
        for i, particle in enumerate(self.particles):
            accel_new = forces_new[i] / particle.mass
            particle.vel += 0.5 * (accel_old[i] + accel_new) * self.dt
        
        self.time += self.dt
    
    def run(self, n_steps: int):
        """Run simulation for n_steps timesteps."""
        for _ in range(n_steps):
            self.step()
