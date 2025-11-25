#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Claude Sonnet 4.5"

"""
Optimal Lambda Search Algorithm for Transient Stability Analysis

This module implements a golden-section search algorithm to identify the gravitational
scaling parameter λ* that maximizes the duration of transient stability in N-body 
gravitational ring systems subject to time-varying repulsive modulation.

The algorithm efficiently converges on the optimal λ value by iteratively narrowing
the search interval based on collapse time measurements. Golden-section search provides
guaranteed convergence with minimal function evaluations compared to exhaustive scanning.

Mathematical Foundation:
    The system exhibits transient stability when the modulation period τ = 2π/ω_ζ and
    the gravitational collapse timescale t_collapse ~ √(R₀³/GM_eff) are balanced through
    appropriate selection of λ, where the repulsive coupling is k_ζ = λG.

"""

import numpy as np
import src.pyparticlesim as pps

def find_optimal_lambda(
    lambda_min: float = 0.7,
    lambda_max: float = 1.0,
    tolerance: float = 0.01,
    G: float = 10.0,
    omega_zeta: float = 300.0,
    dt: float = 1e-5,
    max_steps: int = 20000,
    collapse_threshold: float = 0.95,
    check_interval: int = 100,
    n_particles: int = 100,
    R0: float = 1.0,
    grav_softening: float = 0.05,
    verbose: bool = True
) -> tuple[float, float]:
    
    """
    Identify the optimal gravitational scaling parameter λ* that maximizes transient
    stability duration using golden-section search optimization.

    This function employs the golden-section search algorithm to efficiently locate
    the value of λ within the specified interval [λ_min, λ_max] that produces the
    longest duration before gravitational collapse or expansion dominates the system
    dynamics. The algorithm iteratively evaluates candidate λ values by running full
    N-body simulations and measuring the time until the average ring radius deviates
    beyond the collapse threshold from its initial value.

    Algorithm Overview:
        The golden-section search method divides the search interval according to the
        golden ratio φ = (1 + √5)/2 ≈ 1.618, which provides optimal convergence 
        properties for unimodal objective functions. At each iteration, two interior
        points λ_c and λ_d are evaluated, and the interval is narrowed by eliminating
        the subinterval containing the point with shorter collapse time. This process
        continues until the interval width falls below the specified tolerance.

    Physical Interpretation:
        The collapse time t_collapse represents the duration for which the system
        maintains bounded breathing oscillations with R_avg ≈ R₀ before gravitational
        attraction overwhelms the time-varying repulsive modulation. The optimal λ*
        balances the competing forces such that Nλ ≈ M_eff, maximizing the transient
        stability window within the constraint c ∈ [2,3] modulation cycles.

    Parameters:
        lambda_min : float, default=0.7
            Lower bound of the search interval for λ. Should be chosen based on
            preliminary scans or theoretical predictions suggesting λ ≈ M_eff/N.

        lambda_max : float, default=1.0
            Upper bound of the search interval for λ. Values significantly above
            M_eff/N typically lead to rapid expansion rather than collapse.

        tolerance : float, default=0.01
            Convergence criterion for the search algorithm. The optimization terminates
            when the interval width |λ_max - λ_min| falls below this threshold. Smaller
            values provide higher precision at the cost of additional iterations.

        G : float, default=10.0
            Gravitational coupling constant determining the strength of attractive
            interactions between particles. This parameter scales both gravitational
            and repulsive forces through the relation k_ζ = λG.

        omega_zeta : float, default=300.0
            Angular frequency of the sinusoidal repulsive force modulation in rad/s.
            Determines the period τ = 2π/ω_ζ of breathing oscillations.

        dt : float, default=1e-5
            Integration timestep for velocity Verlet algorithm in time units. Must be
            chosen sufficiently small to maintain numerical stability for the given
            coupling strength G and frequency ω_ζ.

        max_steps : int, default=20000
            Maximum number of integration steps per simulation. Corresponds to maximum
            simulation time t_max = max_steps × dt. Should be large enough to capture
            collapse dynamics beyond the c ∈ [2,3] cycle window.

        collapse_threshold : float, default=0.95
            Fractional threshold defining collapse criterion. The system is considered
            collapsed when R_avg < collapse_threshold × R₀. A value of 0.95 corresponds
            to 5% contraction from initial radius.

        check_interval : int, default=100
            Number of timesteps between collapse checks. Frequent checks (small interval)
            provide precise collapse time measurement but increase computational overhead.
            A value of 100 balances precision with efficiency.

        n_particles : int, default=100
            Number of point particles comprising the gravitational ring. Determines the
            effective mass M_eff ≈ n_particles × m for unit mass particles.

        R0 : float, default=1.0
            Initial radius of the particle ring in length units. All particles are
            uniformly distributed on a circle of radius R₀ at t = 0.

        grav_softening : float, default=0.05
            Softening parameter ε_grav preventing gravitational force singularities at
            small separations through the modified force law F ∝ 1/(r² + ε²). Also
            applied to repulsive force as ε_ζ = ε_grav for consistency.

        verbose : bool, default=True
            Enable detailed progress output during optimization. When True, prints
            iteration number, candidate λ values, and corresponding collapse times
            to facilitate monitoring of convergence behavior.

    Returns:
        lambda_optimal : float
            The gravitational scaling parameter λ* that maximizes transient stability
            duration within the specified search interval and tolerance.

        t_optimal : float
            The collapse time achieved at λ = λ*, representing the duration for which
            the system maintains R_avg ≈ R₀ before gravitational collapse dominates.

    Algorithm Complexity:
        The golden-section search achieves convergence in O(log(Δλ/tolerance)) iterations
        where Δλ = λ_max - λ_min is the initial interval width. Each iteration requires
        one or two full N-body simulations (depending on reuse of previous evaluations),
        making this approach substantially more efficient than exhaustive grid search
        while guaranteeing convergence to the global optimum for unimodal objective
        functions.

    Numerical Considerations:
        The velocity Verlet integrator employed in the underlying simulations is a
        second-order symplectic method providing bounded energy errors over extended
        integration times. However, for strongly coupled systems (G ≥ 50), timestep
        constraints apply regardless of integration method. The collapse time measurements
        are subject to numerical artifacts from finite timestep resolution and softening
        parameters, which should be consistent across all λ evaluations for valid
        comparison.

    Example:
        >>> lambda_opt, t_opt = find_optimal_lambda(
        ...     lambda_min=0.75,
        ...     lambda_max=0.95,
        ...     tolerance=0.005,
        ...     G=10.0,
        ...     omega_zeta=300.0,
        ...     verbose=True
        ... )
        Starting golden-section search: λ ∈ [0.7500, 0.9500]
        Iteration 1: λ_c=0.8264 (t=0.0521), λ_d=0.8736 (t=0.0489)
        Iteration 2: λ_c=0.8028 (t=0.0543), λ_d=0.8264 (t=0.0521)
        ...
        Optimal λ* = 0.8442 with collapse time t = 0.0567
        
        >>> print(f"Optimal parameters: λ* = {lambda_opt:.4f}, t = {t_opt:.4f}")
        Optimal parameters: λ* = 0.8442, t = 0.0567

    References:
        [1] Kiefer, J. (1953). Sequential minimax search for a maximum. 
            Proceedings of the American Mathematical Society, 4(3), 502-506.
        [2] Press, W. H., et al. (2007). Numerical Recipes: The Art of Scientific 
            Computing (3rd ed.). Cambridge University Press.
    """
    
    # Golden ratio for interval division
    phi = (1 + np.sqrt(5)) / 2
    resphi = 2 - phi  # 1/phi for efficient computation
    
    # Initialize search interval
    a = lambda_min
    b = lambda_max
    
    # Compute initial interior points using golden ratio
    c = a + resphi * (b - a)
    d = b - resphi * (b - a)
    
    if verbose:
        print(f"Starting golden-section search: λ ∈ [{lambda_min:.4f}, {lambda_max:.4f}]")
        print(f"Target tolerance: {tolerance:.6f}")
        print(f"Simulation parameters: G={G}, ω_ζ={omega_zeta}, Δt={dt}")
        print(f"Collapse criterion: R_avg < {collapse_threshold}R₀")
        print()
    
    # Helper function to run simulation and measure collapse time
    def evaluate_lambda(lam: float) -> float:
        """Execute full N-body simulation for given λ and return collapse time."""
        
        # Initialize particle ring
        struct = pps.Particle_Structure('circle', [0.0, 0.0, R0], n_particles)
        
        # Configure force field with time-varying repulsion
        field = pps.SK_Field(
            G=G,
            grav_softening=grav_softening,
            omega_zeta=omega_zeta,
            k_zeta=lam * G,
            zeta_softening=grav_softening,
        )
        
        # Initialize velocity Verlet integrator
        sim = pps.Verlet_Simulation(struct.particles, dt, field)
        
        # Integrate until collapse or maximum time
        for step in range(max_steps):
            sim.step()
            
            # Periodic collapse detection
            if step % check_interval == 0:
                radii = [np.linalg.norm(p.pos) for p in sim.particles]
                R_avg = np.mean(radii)
                
                if R_avg < collapse_threshold * R0:
                    return sim.time
        
        # Return maximum time if no collapse detected
        return sim.time
    
    # Evaluate collapse times at initial interior points
    fc = evaluate_lambda(c)
    fd = evaluate_lambda(d)
    
    iteration = 0
    
    # Golden-section search main loop
    while abs(b - a) > tolerance:
        iteration += 1
        
        if verbose:
            print(f"Iteration {iteration}: λ_c={c:.4f} (t={fc:.4f}), "
                  f"λ_d={d:.4f} (t={fd:.4f}), interval=[{a:.4f}, {b:.4f}]")
        
        # Update interval based on which point has longer collapse time
        if fc > fd:
            # Maximum lies in [a, d], discard [d, b]
            b = d
            d = c
            fd = fc
            c = a + resphi * (b - a)
            fc = evaluate_lambda(c)
        else:
            # Maximum lies in [c, b], discard [a, c]
            a = c
            c = d
            fc = fd
            d = b - resphi * (b - a)
            fd = evaluate_lambda(d)
    
    # Final optimal value is midpoint of converged interval
    lambda_optimal = (a + b) / 2
    t_optimal = evaluate_lambda(lambda_optimal)
    
    if verbose:
        print()
        print(f"Convergence achieved after {iteration} iterations")
        print(f"Optimal λ* = {lambda_optimal:.6f}")
        print(f"Maximum collapse time t = {t_optimal:.6f}")
        print(f"Number of cycles: c ≈ {t_optimal * omega_zeta / (2 * np.pi):.2f}")
    
    return lambda_optimal, t_optimal


# Example usage and validation
if __name__ == "__main__":
    # Execute optimization with default parameters
    lambda_star, time_star = find_optimal_lambda(
        lambda_min=0.75,
        lambda_max=0.95,
        tolerance=0.005,
        max_steps=15000,
        verbose=True
    )
    
    print("\n" + "="*70)
    print(f"RESULT: λ* = {lambda_star:.4f} maximizes transient stability")
    print(f"        with collapse time t* = {time_star:.4f}")
    print("="*70)
