#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Kamyar Modjtahedzadeh"

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
        
        self.pos = np.array(position, dtype=float)   # [x, y]
        self.vel = np.array(velocity, dtype=float)   # [vx, vy]
        self.mass = mass
        self.radius = radius
        self.force = np.array([0.0, 0.0])            # [fx, fy] accumulator

    #def reset_force(self):
    #    self.force = np.array([0.0, 0.0])

    def advance(self, dt, method='euler'):
        """Update position and velocity using accumulated forces."""
        if method == 'euler':
            self._advance_euler(dt)
        elif method == 'verlet':
            self._advance_verlet(dt)
            # For Verlet, we'll need to store self.accel_prev (previous acceleration).
            # We must add that attribute to __init__ and initialize it to zero.
        elif method == 'rk4':
            self._advance_rk4(dt)
        else:
            raise ValueError(f"Unknown integration method: {method}")
    
    def _advance_euler(self, dt):
        acceleration = self.force/self.mass
        self.vel += acceleration*dt
        self.pos += self.vel*dt

    def apply_forces(self, dt, *forces, method='euler'):
        """Apply forces, advance particle, then reset force accumulator."""
        forces = np.array(forces)     # Make sure array of forces is a NumPy array
        self.force[:] = 0.0
        for f in forces:
            self.force += f
        self.advance(dt, method=method)
        self.force[:] = 0.0


class Simulation:
    """
    2D particle simulation engine with force accumulation and time-stepping.

    USELSESS as of now:
        Simulation.step() incompatible with SK_Field.compute_forces() which returns 
        pre-computed force arrays instead of per-particle force functions.
    """
    
    def __init__(self, particles, dt):
        self.particles = np.array(particles)  # Array of Particle objects
        self.dt = dt
        self.time = 0.0

    def step(self, *force_funcs):
        """Advance simulation by one timestep."""
        for particle in self.particles:
            forces = []
            for f in force_funcs:
                if callable(f):
                    forces.append(f(particle))
                else:
                    forces.append(f)  # Pre-computed array
            particle.apply_forces(self.dt, *forces)
        self.time += self.dt
    
    def run(self, n_steps: int, *forces):
        """Run simulation for n_steps."""
        for _ in range(n_steps):
            self.step(*forces)


class Particle_Structure:
    """Generate initial particle configurations in various geometric structures."""

    def __init__(self, structure='circle', init_points=None, nParticles=10, particle_vel=(0.0, 0.0), particle_mass=1.0, particle_radius=1.0):
        if init_points is None:
            raise ValueError("init_points cannot be None")
        
        # Uniform structure properties
        self.particle_vel = particle_vel
        self.particle_mass = particle_mass
        self.particle_radius = particle_radius
        
        init_points = np.array(init_points).flatten()
    
        if structure == 'circle':
            if len(init_points) != 3:
                raise ValueError("Circle structure requires 3 values: [center_x, center_y, radius]")
            self.particles = self.gen_circle(init_points, nParticles)           
        elif structure == 'line':
            if len(init_points) != 4:
                raise ValueError("Line structure requires 4 values: [start_x, start_y, end_x, end_y]")
            self.particles = self.gen_line(init_points, nParticles)
        elif structure == 'rectangle':
            if len(init_points) != 4:
                raise ValueError("Rectangle structure requires 4 values: [bottom_left_x, bottom_left_y, x_length, y_length]")
            self.particles = self.gen_rectangle(init_points, nParticles)
        elif structure == 'diamond':
            if len(init_points) != 4:
                raise ValueError("Diamond structure requires 4 values: [center_x, center_y, x_length, y_length]")
            self.particles = self.gen_diamond(init_points, nParticles)
        elif structure == 'solid_circle':
            if len(init_points) != 3:
                raise ValueError("Solid circle structure requires 3 values: [center_x, center_y, radius]")
            self.particles = self.gen_solid_circle(init_points, nParticles)
        elif structure == 'solid_diamond':
            if len(init_points) != 4:
                raise ValueError("Solid diamond structure requires 4 values: [center_x, center_y, x_length, y_length]")
            self.particles = self.gen_solid_diamond(init_points, nParticles)
        elif structure == 'tilted_rectangle':
            raise NotImplementedError('Diamond structure not implemented yet')
        else:
            raise ValueError(f"Unknown structure: {structure}")

    def gen_circle(self, init_points, nParticles):
        """Generate particles uniformly distributed on a circle."""
        center_x, center_y, circle_radius = init_points
        φ = np.linspace(0, 2*np.pi, nParticles, endpoint=False)
        x = center_x + circle_radius*np.cos(φ)
        y = center_y + circle_radius*np.sin(φ)
        particles = np.array([Particle(position=[x[i], y[i]], velocity=self.particle_vel, mass=self.particle_mass, radius=self.particle_radius) for i in range(nParticles)])
        #return np.array([particle.pos for particle in particles])   # Return positions only
        return particles

    def gen_diamond(self, init_points, nParticles, tilt=None):
        """
        Generate particles uniformly distributed on diamond perimeter.
        
        Diamond with horizontal and vertical diagonals aligned with axes.
        
        Args:
            init_points: [center_x, center_y, x_length, y_length] where x_length is full width, y_length is full height
            nParticles: total number of particles to distribute
            tilt: reserved for future rotation (not implemented)
        """
        
        center_x, center_y, x_length, y_length = init_points
        
        # Four vertices
        top = np.array([center_x, center_y + y_length/2])
        right = np.array([center_x + x_length/2, center_y])
        bottom = np.array([center_x, center_y - y_length/2])
        left = np.array([center_x - x_length/2, center_y])
        
        # Side lengths
        side_top_right = np.linalg.norm(right - top)
        side_right_bottom = np.linalg.norm(bottom - right)
        side_bottom_left = np.linalg.norm(left - bottom)
        side_left_top = np.linalg.norm(top - left)
        perimeter = side_top_right + side_right_bottom + side_bottom_left + side_left_top
        
        # Distribute particles proportionally
        n_top_right = int(nParticles * side_top_right / perimeter)
        n_right_bottom = int(nParticles * side_right_bottom / perimeter)
        n_bottom_left = int(nParticles * side_bottom_left / perimeter)
        n_left_top = nParticles - (n_top_right + n_right_bottom + n_bottom_left)
        
        # Top to Right
        x_tr = np.linspace(top[0], right[0], n_top_right, endpoint=False)
        y_tr = np.linspace(top[1], right[1], n_top_right, endpoint=False)
        
        # Right to Bottom
        x_rb = np.linspace(right[0], bottom[0], n_right_bottom, endpoint=False)
        y_rb = np.linspace(right[1], bottom[1], n_right_bottom, endpoint=False)
        
        # Bottom to Left
        x_bl = np.linspace(bottom[0], left[0], n_bottom_left, endpoint=False)
        y_bl = np.linspace(bottom[1], left[1], n_bottom_left, endpoint=False)
        
        # Left to Top
        x_lt = np.linspace(left[0], top[0], n_left_top, endpoint=False)
        y_lt = np.linspace(left[1], top[1], n_left_top, endpoint=False)
        
        # Concatenate
        x = np.concatenate([x_tr, x_rb, x_bl, x_lt])
        y = np.concatenate([y_tr, y_rb, y_bl, y_lt])
        
        particles = np.array([
            Particle(
                position=[x[i], y[i]], 
                velocity=self.particle_vel, 
                mass=self.particle_mass, 
                radius=self.particle_radius
            ) for i in range(nParticles)
        ])
        
        return particles

    def gen_line(self, init_points, nParticles):
        """Generate particles uniformly distributed along a line segment."""
        start_x, start_y, end_x, end_y = init_points
        x = np.linspace(start_x, end_x, nParticles)
        y = np.linspace(start_y, end_y, nParticles)
        particles = np.array([Particle(position=[x[i], y[i]], velocity=self.particle_vel, mass=self.particle_mass, radius=self.particle_radius) for i in range(nParticles)])
        #return np.array([particle.pos for particle in particles])   # Return positions only
        return particles

    def gen_rectangle(self, init_points, nParticles, tilt=None):
        """Generate particles uniformly distributed on rectangle perimeter."""
        
        bottom_left_x, bottom_left_y, x_length, y_length = init_points
        
        # Calculate perimeter
        perimeter = 2*(x_length + y_length)
        # Distribute particles proportionally along each side
        n_bottom = int(nParticles*x_length/perimeter)
        n_right  = int(nParticles*y_length/perimeter)
        n_top    = int(nParticles*x_length/perimeter)
        n_left   = nParticles - (n_bottom + n_right + n_top)  # Remainder
        # Bottom side
        x_bottom = np.linspace(bottom_left_x, bottom_left_x + x_length, n_bottom, endpoint=False)
        y_bottom = np.full(n_bottom, bottom_left_y)
        # Right side
        x_right = np.full(n_right, bottom_left_x + x_length)
        y_right = np.linspace(bottom_left_y, bottom_left_y + y_length, n_right, endpoint=False)
        # Top side
        x_top = np.linspace(bottom_left_x + x_length, bottom_left_x, n_top, endpoint=False)
        y_top = np.full(n_top, bottom_left_y + y_length)
        # Left side
        x_left = np.full(n_left, bottom_left_x)
        y_left = np.linspace(bottom_left_y + y_length, bottom_left_y, n_left, endpoint=False)
        # Concatenate all sides
        x = np.concatenate([x_bottom, x_right, x_top, x_left])
        y = np.concatenate([y_bottom, y_right, y_top, y_left])
        
        particles = np.array([Particle(position=[x[i], y[i]], velocity=self.particle_vel, mass=self.particle_mass, radius=self.particle_radius) for i in range(nParticles)])
        return particles

    def gen_solid_circle(self, init_points, nParticles):
        """
        Generate particles uniformly distributed inside a solid circle.
        
        Uses square root sampling for uniform area distribution.
        
        Args:
            init_points: [center_x, center_y, radius]
            nParticles: total number of particles to distribute
        """
        
        center_x, center_y, radius = init_points
        
        # Uniform sampling in polar coordinates
        # r ~ sqrt(U[0,1]) for uniform area density
        # φ ~ U[0, 2π]
        r = radius * np.sqrt(np.random.uniform(0, 1, nParticles))
        φ = np.random.uniform(0, 2*np.pi, nParticles)
        
        x = center_x + r * np.cos(φ)
        y = center_y + r * np.sin(φ)
        
        particles = np.array([
            Particle(
                position=[x[i], y[i]], 
                velocity=self.particle_vel, 
                mass=self.particle_mass, 
                radius=self.particle_radius
            ) for i in range(nParticles)
        ])
        
        return particles

    def gen_solid_diamond(self, init_points, nParticles, tilt=None):
        """
        Generate particles uniformly distributed inside a solid diamond.
        
        Uses rejection sampling within bounding box.
        
        Args:
            init_points: [center_x, center_y, x_length, y_length]
            nParticles: total number of particles to distribute
            tilt: reserved for future rotation (not implemented)
        """
        
        center_x, center_y, x_length, y_length = init_points
        
        particles = []
        while len(particles) < nParticles:
            # Sample from bounding box
            x = np.random.uniform(center_x - x_length/2, center_x + x_length/2)
            y = np.random.uniform(center_y - y_length/2, center_y + y_length/2)
            
            # Check if inside diamond: |Δx|/half_width + |Δy|/half_height ≤ 1
            if abs(x - center_x)/(x_length/2) + abs(y - center_y)/(y_length/2) <= 1:
                particles.append(
                    Particle(
                        position=[x, y], 
                        velocity=self.particle_vel, 
                        mass=self.particle_mass, 
                        radius=self.particle_radius
                    )
                )
        
        return np.array(particles)
    