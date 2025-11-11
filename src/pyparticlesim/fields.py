#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Kamyar Modjtahedzadeh"

try:
    # If imported from ~/workspace
    from src.pyparticlesim.particles_and_structures import Particle
except ImportError:
    # If imported from ~/workspace/src
    from pyparticlesim.particles_and_structures import Particle
except ImportError:
    # If imported from ~/workspace/src/pyparticlesim
    from particles_and_structures import Particle

import numpy as np


class SK_Field:
    """
    Stateless field class for computing particle-particle interaction forces.

    Computes N-body forces based on provided parameters. Supports multiple
    force types simultaneously (gravity, attractive force, etc.).
    """

    def __init__(self, **params):
        """
        Args:
            **params: Force parameters (e.g., G, grav_softening, k_attractive, attractive_softening)
        """

        self.params = params

    def compute_forces(self, particles, time=0.0):
        """
        Compute all pairwise forces for particle array.

        Args:
            particles: Array of Particle objects
            time: Current simulation time (for time-varying forces)

        Returns:
            Array of force vectors [Fx, Fy] for each particle
        """

        n = len(particles)
        forces = np.zeros((n, 2))

        # Double loop over particle pairs
        for i in range(n):
            for j in range(i + 1, n):
                # Compute pairwise force
                f_ij = self._pairwise_force(particles[i], particles[j], time)

                # Newton's third law
                forces[i] += f_ij
                forces[j] -= f_ij

        return forces

    def _pairwise_force(self, p1, p2, time):
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

        if 'k_repulsive' in self.params:
            f_total += self._repulsive(p1, p2, r, r_hat)

        if 'k_zeta' in self.params:
            f_total += self._time_varying_repulsive(p1, p2, r, r_hat, time)

        return f_total

    def _gravity(self, p1, p2, r, r_hat):
        """
        N-body gravitational force with softening.

            Models mutual gravitational attraction between massive particles. Newton's law of universal gravitation 
            describes the attractive force between any two masses.

                $$
                \vec{F}_{\mathrm{grav}} = -\frac{Gm_1m_2}{r^2 + \epsilon^2}\hat{r}
                $$

            where $\hat{r} = \frac{\vec{r}_1 - \vec{r}_2}{r}$ and $r = |\vec{r}_1 - \vec{r}_2|$, $G$ is the 
            gravitational constant, $\epsilon$ is the softening length, and $m_1$, $m_2$ are particle masses. 
            Softening prevents numerical divergence at small separations.
        """

        G = self.params['G']
        epsilon = self.params.get('grav_softening', 0.01)
        return -G * p1.mass * p2.mass / (r**2 + epsilon**2) * r_hat

    def _repulsive(self, p1, p2, r, r_hat):
        """
        Softened repulsive force with configurable exponent:

            Models a general repulsive interaction between particles with softening to prevent singularities.
            This force opposes gravitational collapse and can represent electrostatic repulsion, degeneracy 
            pressure, or contact forces.
            
                $$
                \vec{F}_{\mathrm{repulsive}} = +\frac{|k_{\mathrm{r}}|}{r^\alpha + \epsilon_{\mathrm{r}}^\alpha} \hat{r}
                $$
            
            where $\hat{r} = \frac{\vec{r}_1 - \vec{r}_2}{r}$ and $r = |\vec{r}_1 - \vec{r}_2|$, $k_{\mathrm{r}}$ is the 
            repulsive coupling constant, $\epsilon_{\mathrm{r}}$ is the repulsive softening length, and $\alpha$ is the 
            power-law exponent (default: 2 for inverse-square).
            The positive sign creates repulsion (particles push apart). Softening prevents numerical divergence 
            at small separations.
        """
        
        k_r = self.params['k_repulsive']
        epsilon_r = self.params.get('repulsive_softening', 0.01)
        α = self.params.get('repulsive_exponent', 2)
        return np.abs(k_r) / (r**α + epsilon_r**α) * r_hat

    def _time_varying_repulsive(self, p1, p2, r, r_hat, time):
        """
        Time-varying repulsive force for breathing oscillations:

            Models periodic modulation of repulsion strength to induce expansion-contraction cycles 
            in N-body systems. The force magnitude varies sinusoidally with time.
            
                $$
                \vec{F}_{\zeta} = |k_{\zeta}| \cdot \frac{\zeta(t)}{r^2 + \epsilon_{\zeta}^2} \hat{r}
                $$
            
            where the modulating signal follows:
            
                $$
                \zeta(t) = 1 + A\sin(\omega t)
                $$
            
            with $\hat{r} = \frac{\vec{r}_1 - \vec{r}_2}{r}$ and $r = |\vec{r}_1 - \vec{r}_2|$, $k_{\zeta}$ is the 
            repulsive coupling constant, $\epsilon_{\zeta}$ is the softening length, $A$ is the modulation 
            amplitude (0 < A ≤ 1), and $\omega$ is the angular frequency.
            The time-dependent modulation creates breathing oscillations in the particle system.
        """
        
        k_zeta = self.params['k_zeta']
        epsilon_zeta = self.params.get('zeta_softening', 0.01)
        A = self.params.get('zeta_amplitude', 0.5)
        omega = self.params.get('omega_zeta', 1.0)
        
        # Compute modulating signal ζ(t)
        zeta_t = 1.0 + A * np.sin(omega * time)
        
        return np.abs(k_zeta) * zeta_t / (r**2 + epsilon_zeta**2) * r_hat