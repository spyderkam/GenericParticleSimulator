# Overview of Plots

These plots show a ring of 100 identical point particles with unit mass under coupled gravitational attraction and sinusoidal repulsive modulation. The governing equation is:

$$\mathbf{F}*{\mathrm{total}}(t) = \mathbf{F}^\prime*{\mathrm{grav}} + \mathbf{F}_\zeta(t)$$

where

$$\mathbf{F}^\prime_{\mathrm{grav}} = -G \cdot \frac{m_i m_j}{r_{ij}^2 + \epsilon_{\mathrm{grav}}^2}\hat{r}_{ij}$$

$$\mathbf{F}*\zeta(t) = |k*\zeta| \cdot \frac{\zeta(t)}{r_{ij}^2 + \epsilon_\zeta^2}\hat{r}_{ij}$$

with modulating signal:

$$\zeta(t) = 1 + \sin(\omega_\zeta t)$$

## Dynamics

The ring exhibits **transient breathing oscillations**: initial expansion as repulsive modulation dominates, followed by contraction as gravitational potential overwhelms the time-varying repulsive force, culminating in gravitational collapse. The sequence (2000→8000 steps) documents this progression from stable breathing through decay to collapse.

Plots generated using [velocity Verlet](https://github.com/spyderkam/GenericParticleSimulator/blob/main/src/pyparticlesim/verlet_simulation.py) integration.

## Parameters

```python
G = 10.0
grav_softening = 0.05
lambda_ = 0.843
k_zeta = lambda_ * G
zeta_softening = grav_softening
omega_zeta = 300
dt = 1e-5
```

Filename `breathing_oscillations_verlet_<n_steps>.pdf` indicates timestep count; legend shows simulation end time.​​​​​​​​​​​​​​​​