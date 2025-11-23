# Derivation of Generalized Virial Theorem

## Introduction

The **generalized virial theorem** is a fundamental result in classical mechanics that relates the kinetic energy of a system to the forces acting on its constituent particles. Unlike the classical virial theorem (which applies only to time-independent, conservative systems), the generalized form handles arbitrary time-dependent forces.

## Derivation

### Step 1: Define the Moment of Inertia

For a system of $N$ particles with masses $m_i$ and position vectors $\vec{r}_i$, define the **scalar moment of inertia**:

$$I = \sum_{i=1}^{N} m_i r_i^2 = \sum_{i=1}^{N} m_i \vec{r}_i \cdot \vec{r}_i$$

### Step 2: First Time Derivative

Taking the first derivative with respect to time:

$$\frac{dI}{dt} = \sum_i m_i \frac{d}{dt}(\vec{r}_i \cdot \vec{r}_i) = \sum_i m_i \left(2\vec{r}_i \cdot \frac{d\vec{r}_i}{dt}\right) = 2\sum_i m_i \vec{r}_i \cdot \vec{v}_i$$

where $\vec{v}_i = d\vec{r}_i/dt$ is the velocity of particle $i$.

### Step 3: Second Time Derivative

Taking the second derivative:

$$\frac{d^2I}{dt^2} = 2\sum_i m_i \frac{d}{dt}\left(\vec{r}_i \cdot \vec{v}_i\right)$$

Using the product rule:

$$\frac{d^2I}{dt^2} = 2\sum_i m_i \left(\vec{v}_i \cdot \vec{v}_i + \vec{r}_i \cdot \frac{d\vec{v}_i}{dt}\right)$$

$$= 2\sum_i m_i v_i^2 + 2\sum_i m_i \vec{r}_i \cdot \vec{a}_i$$

where $\vec{a}_i = d\vec{v}_i/dt$ is the acceleration.

### Step 4: Apply Newton's Second Law

By Newton's second law, $m_i \vec{a}_i = \vec{F}_i$, where $\vec{F}_i$ is the total force on particle $i$. Substituting:

$$\frac{d^2I}{dt^2} = 2\sum_i m_i v_i^2 + 2\sum_i \vec{r}_i \cdot \vec{F}_i$$

### Step 5: Relate to Kinetic Energy

The total kinetic energy is:

$$T = \sum_i \frac{1}{2}m_i v_i^2$$

Therefore:

$$\sum_i m_i v_i^2 = 2T$$

### Step 6: Final Form

Substituting into our expression:

$$\boxed{\frac{d^2I}{dt^2} = 4T - \sum_i \vec{r}_i \cdot \vec{F}_i}$$

This is the **generalized virial theorem** in its exact form.

## Interpretation

- **Left side**: Second time derivative of the moment of inertia (measures expansion/contraction of the system)
- **Right side**: Balance between kinetic energy ($4T$) and the virial of forces ($-\sum_i \vec{r}_i \cdot \vec{F}_i$)

### Time-Averaged Form

For systems in quasi-equilibrium (periodic motion without secular drift), time-averaging over a period $\tau$ gives:

$$\left\langle\frac{d^2I}{dt^2}\right\rangle = \frac{1}{\tau}\int_0^\tau \frac{d^2I}{dt^2}\,dt = \frac{1}{\tau}\left[\frac{dI}{dt}\bigg|_\tau - \frac{dI}{dt}\bigg|_0\right]$$

For periodic motion, $dI/dt$ returns to its initial value, so:

$$\left\langle\frac{d^2I}{dt^2}\right\rangle = 0$$

This yields the **time-averaged virial condition**:

$$\boxed{2\langle T \rangle = \left\langle\sum_i \vec{r}_i \cdot \vec{F}_i\right\rangle}$$

## Application to Conservative Forces

For conservative forces derivable from a potential $U(\vec{r}_1, \ldots, \vec{r}_N)$:

$$\vec{F}_i = -\nabla_i U$$

### Homogeneous Potentials

If $U$ is a **homogeneous function of degree $n$**&mdash;meaning $U(\alpha \vec{r} _1, \dots, \alpha \vec{r} _N) = \alpha^n U(\vec{r} _1, \dots, \vec{r} _N)$&mdash;then by Euler's theorem:

$$\sum_i \vec{r}_i \cdot \nabla_i U = n U$$

For example:
- Gravitational potential: $U \propto 1/r$ → $n = -1$
- Harmonic potential: $U \propto r^2$ → $n = 2$

This gives:

$$\sum_i \vec{r}_i \cdot \vec{F}_i = -n U$$

For time-averaged equilibrium with homogeneous potentials:

$$2\langle T \rangle = -n \langle U \rangle$$

For gravity ($n = -1$):

$$2\langle T \rangle = \langle U \rangle \quad \text{or} \quad 2\langle T \rangle + \langle U \rangle = 0$$

This recovers the **classical virial theorem** as a special case.

## References

1. **Goldstein, H., Poole, C., & Safko, J.** (2002). *Classical Mechanics* (3rd ed.). Addison-Wesley. Chapter 3, Section 3.4: "The Virial Theorem."

2. **Collins, G. W.** (1978). *The Virial Theorem in Stellar Astrophysics*. Pachart Publishing House. Chapter 2: "Derivation of the Tensor Virial Theorem."

3. **Landau, L. D., & Lifshitz, E. M.** (1976). *Mechanics* (3rd ed.). Butterworth-Heinemann. Section 10: "The virial theorem."

4. **Binney, J., & Tremaine, S.** (2008). *Galactic Dynamics* (2nd ed.). Princeton University Press. Section 4.8.2: "The virial theorem."

5. **Parker, E. N.** (1954). Tensor virial equations. *Physical Review*, 96(6), 1686-1689.
