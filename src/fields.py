#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Kamyar Modjtahedzadeh"

from src.particles_and_structures import Particle
import numpy as np


class SK_Field:
    """
    Stateless field class for computing particle-particle interaction forces.
    
    Computes N-body forces based on provided parameters. Supports multiple
    force types simultaneously (gravity, Lennard-Jones, springs, etc.).
    """

    def __init__(self, **params):
        """
        Args:
            **params: Force parameters (e.g., G, epsilon, sigma, k, cutoff)
        """
        
        self.params = params

    def compute_forces(self, particles):
        """
        Compute all pairwise forces for particle array.
        
        Args:
            particles: Array of Particle objects
            
        Returns:
            Array of force vectors [Fx, Fy] for each particle
        """
        
        n = len(particles)
        forces = np.zeros((n, 2))
        
        # Double loop over particle pairs
        for i in range(n):
            for j in range(i + 1, n):
                # Compute pairwise force
                f_ij = self._pairwise_force(particles[i], particles[j])
                
                # Newton's third law
                forces[i] += f_ij
                forces[j] -= f_ij
        
        return forces
    
    def _pairwise_force(self, p1, p2):
        """
        Compute force on p1 due to p2.
        
        Checks self.params to determine which forces to include.
        """
        
        # Relative position
        r_vec = p1.pos - p2.pos
        r = np.linalg.norm(r_vec)
        
        if r == 0:
            return np.array([0.0, 0.0])
        
        r_hat = r_vec / r
        f_total = np.array([0.0, 0.0])
        
        if 'G' in self.params:
            f_total += self._gravity(p1, p2, r, r_hat)
        
        if 'epsilon' in self.params and 'sigma' in self.params:
            f_total += self._lennard_jones(p1, p2, r, r_hat)
        
        return f_total

    def _gravity(self, p1, p2, r, r_hat):
        """
        N-body gravitational force:
    
            Models mutual gravitational attraction between massive particles. Newton's law of universal gravitation 
            describes the attractive force between any two masses.
            
                $$
                \vec{F}_{\mathrm{grav}} = -\frac{Gm_1m_2}{r^2}\hat{r}
                $$
            
            where $\hat{r} = \frac{\vec{r}_1 - \vec{r}_2}{r}$ and $r = |\vec{r}_1 - \vec{r}_2|$, $G$ is the 
            gravitational constant, and $m_1$, $m_2$ are particle masses. Negative sign indicates attraction.
        """
        G = self.params['G']
        return -G * p1.mass * p2.mass / r**2 * r_hat

    def _lennard_jones(self, p1, p2, r, r_hat):
        """
        Lennard-Jones potential:

            Used fo modeling van der Waals interactions between neutral atoms/molecules. van der Waals interactions are 
            weak intermolecular forces from temporary charge fluctuations (dipole interactions). Attraction between 
            neutral molecules/atoms.
            
                $$
                \vec{F}_{\mathrm{LJ}} = \frac{24\epsilon}{r}\left[2\left(\frac{\sigma}{r}\right)^{13} - \left(\frac{\sigma}{r}\right)^7\right]\hat{r}
                $$
            
            where $\hat{r} = \frac{\vec{r}_1 - \vec{r}_2}{r}$ and $r = |\vec{r}_1 - \vec{r}_2|$, $\epsilon$ is the depth
            of potential well (bond strength). and $\sigma$ is the distance where potential is zero (particle diameter)
        """
        
        epsilon = self.params['epsilon']
        sigma = self.params['sigma']
        sigma_over_r = sigma / r
        return 24 * epsilon * (2 * sigma_over_r**13 - sigma_over_r**7) / r * r_hat
