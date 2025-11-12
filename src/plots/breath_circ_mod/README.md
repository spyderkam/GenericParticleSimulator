# Overview of Plots

These plots are of what is originally a ring of 100 identical point particles with unit mass. The governing equation of motion is:

$$ \mathbf{F} _{\mathrm{total}}(t) = \mathbf{F}^\prime _{\mathrm{grav}} + \mathbf{F} _{\zeta}(t) $$

where the interparticle gravitational force is

$$ \mathbf{F}^{\prime} _{\mathrm{grav}} = -G \cdot \frac{m_i m_j}{r _{ij}^{2} + \epsilon _{\mathrm{grav}}^2}  \hat{r} _{ij} $$

and the internal modulating repulsive force is:

$$ \mathbf{F} _{\zeta}(t) = \left\vert{k _{\zeta}}\right\vert \cdot \frac{\zeta(t)}{r _{ij}^{2} + \epsilon_{\zeta}^2} \hat{r} _{ij} $$

The modulating signal follows a sinusoidal form:

$$ \zeta(t) = 1 + A\sin(\omega _\zeta t) $$

The plots are created using the [velocity Verlet](https://github.com/spyderkam/GenericParticleSimulator/blob/main/src/pyparticlesim/verlet_simulation.py) method/script.

## Parameters

```python
G = 10.0                    # Tested with grav_softening=0.05, dt=1e-5
grav_softening = 0.05       # Tested with G=10, dt=1e-5
G_scaling_factor = 1/3      # Use to scale k_zeta based on G
k_zeta = G*G_scaling_factor
zeta_softening = 0.05
zeta_amplitude = 1.0        # Increased from 0.5
omega_zeta = 80             # ~1 cycle per 8000 steps of dt=1e-5
dt = 1e-5                   # Tested with G=10, grav_softening=0.05
```

Please note that the plots are named as "breathing_oscillations_verlet_`<n_steps>`.pdf" where `n_steps` is the number of timesteps that the integration was iterrated over. (This can also be deduced from the plot legend.)
