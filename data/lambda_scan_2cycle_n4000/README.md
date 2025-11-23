# Parameters

Average radius $R_{\mathrm{avg}}$ and standard deviation $\sigma_R$ after 1 cycle for different $\lambda$ values. Arrays in format $(\lambda, R_{\mathrm{avg}}, \sigma_R)$.

```python
# Fixed parameters
G = 10.0
grav_softening = 0.05
omega_zeta = 300
dt = 1e-5
n_steps = 4000  # ~2 cycle at ω_ζ=300 (c ≈ 1.91)
n_particles = 100

# Scan parameters
lambda_values = np.linspace(0.8, 0.9, 10)
```