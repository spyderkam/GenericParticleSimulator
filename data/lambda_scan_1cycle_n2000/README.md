# Parameters

Average radius $R_{\mathrm{avg}}$ and standard deviation $\sigma_R$ after 1 cycle for different $\lambda$ values. Arrays in format $(\lambda, R_{\mathrm{avg}}, \sigma_R)$.

```python
# Fixed parameters
G = 10.0
grav_softening = 0.05
omega_zeta = 300
dt = 1e-5
n_steps = 2000  # ~1 cycle at ω_ζ=300 (c ≈ 0.95)
n_particles = 100

# Scan parameters
lambda_values = np.linspace(0.5, 2.0, 20)
```

## Text Output

```
λ=0.500: R_avg=0.955, R_std=0.000
λ=0.579: R_avg=0.970, R_std=0.000
λ=0.658: R_avg=0.985, R_std=0.000
λ=0.737: R_avg=1.000, R_std=0.000
λ=0.816: R_avg=1.014, R_std=0.000
λ=0.895: R_avg=1.028, R_std=0.000
λ=0.974: R_avg=1.043, R_std=0.000
λ=1.053: R_avg=1.057, R_std=0.000
λ=1.132: R_avg=1.071, R_std=0.000
λ=1.211: R_avg=1.085, R_std=0.000
λ=1.289: R_avg=1.099, R_std=0.000
```

## Interpretation

Linear trend: $R_{\mathrm{avg}} \approx 0.91 + 0.13\lambda$ (no plateau).

**Critical constraint:** Systems must stabilize within ~3 cycles or collapse/expand (Section 2).

$\lambda = 0.737$ is the **only candidate** showing $R_{\mathrm{avg}} = 1.0$ after 1 cycle.

### Next Steps

1. **Test λ = 0.737 at 6000 steps** (3 cycles) to check persistence
2. If stable → implement trajectory recording for $R(t)$ analysis
3. If unstable → extend scan below λ = 0.5 to find collapse regime

Run this:
```python
lambda_ = 0.737
n_steps = 6000  # 3 cycles
```

### Results

For `λ=0.737: R_avg=0.777, R_std=0.000`, **collapse confirmed.** Ring contracted from R₀ = 1.0 to R_avg = 0.777 by cycle 3. λ = 0.737 shows transient stability for ~1 cycle, then gravitational collapse dominates.

**Action to take:** To stay within the $c \in [2,3]$ stability window, test the stability for:

```python
lambda_values = np.linspace(0.8, 0.9, 10)
n_steps = 4000  # c ≈ 1.91
```
