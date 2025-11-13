# Mathematical Analysis of Force Scaling in Breathing Oscillations

## Abstract

We present a detailed mathematical analysis of the `G_scaling_factor` parameter in N-body systems with competing gravitational attraction and time-varying repulsion. Through phase space analysis, energy considerations, and perturbative methods, we investigate the stability conditions for periodic oscillations versus secular expansion in self-gravitating systems with modulated internal pressure.

---

## 1. System Definition

### 1.1 Force Balance

The total force on particle $i$ due to particle $j$ is:

$$\vec{F}_{ij}(t) = \vec{F}_{\mathrm{grav}} + \vec{F}_{\zeta}(t)$$

where:

**Gravitational attraction:**

$$\vec{F}_{\mathrm{grav}} = -\frac{Gm_i m_j}{r_{ij}^2 + \epsilon_g^2} \hat{r}_{ij}$$

**Time-varying repulsion:**

$$\vec{F}_{\zeta}(t) = +\frac{|k_\zeta| \zeta(t)}{r_{ij}^2 + \epsilon_\zeta^2} \hat{r}_{ij}$$

**Modulation function:**

$$\zeta(t) = 1 + A\sin(\omega_\zeta t)$$

### 1.2 Parameterization

In our system:
- $m_i = m_j = 1$ (unit masses)
- $\epsilon_g = \epsilon_\zeta = 0.05$ (equal softening)
- $A = 1.0$ (full modulation amplitude)
- $k_\zeta = \lambda G$ where $\lambda$ is the `G_scaling_factor`

The key question: **What value of $\lambda$ produces stable periodic oscillations?**

---

## 2. Simplified Radial Analysis

### 2.1 Single-Particle Approximation

Consider a test particle at radius $R(t)$ from the system's center of mass. The radial equation of motion in the limit where softening is negligible ($\epsilon \ll R$) becomes:

$$\ddot{R} = -\frac{GM_{\mathrm{enc}}}{R^2} + \frac{\lambda G \zeta(t)}{R^2}$$

where $M_{\mathrm{enc}}$ is the enclosed mass. For a uniform ring, this simplifies to:

$$\ddot{R} = \frac{G}{R^2}\left[\lambda\zeta(t) - M_{\mathrm{enc}}\right]$$

### 2.2 Equilibrium Condition

For a **static equilibrium** at $R = R_0$, we require:

$$\lambda\zeta(t) = M_{\mathrm{enc}}$$

Since $\langle \zeta(t) \rangle = 1$ (time-averaged modulation), the time-averaged equilibrium requires:

$$\lambda = M_{\mathrm{enc}}$$

For our system with $M_{\mathrm{enc}} = M_{\mathrm{total}}$ (considering contributions from all particles), this suggests $\lambda = 1$ should provide balance. **However, this is a time-averaged, linear analysis that neglects nonlinear dynamics.**

---

## 3. Nonlinear Oscillation Theory

### 3.1 Perturbation Expansion

Let $R(t) = R_0 + \delta R(t)$ where $|\delta R| \ll R_0$. Expanding to first order in $\delta R$:

$$\ddot{\delta R} + \omega_0^2 \delta R = \frac{G\lambda}{R_0^2}\left[\zeta(t) - \langle\zeta\rangle\right]$$

where the natural frequency is:

$$\omega_0^2 = \frac{2G}{R_0^3}\left[\lambda - M_{\mathrm{enc}}\right]$$

The driving term is:

$$F_{\mathrm{drive}}(t) = \frac{G\lambda A}{R_0^2}\sin(\omega_\zeta t)$$

### 3.2 Resonance Condition

This is a **forced harmonic oscillator**. The particular solution has amplitude:

$$\delta R_{\mathrm{amp}} = \frac{GA\lambda/R_0^2}{\omega_0^2 - \omega_\zeta^2}$$

**Critical observation:** If $\omega_0 \approx \omega_\zeta$, the system exhibits resonance with unbounded amplitude growth (in the linear approximation).

### 3.3 Frequency Matching

From simulations, $\omega_\zeta = 157.08$ rad/s corresponds to one oscillation per $n \times dt = 4000 \times 10^{-5} = 0.04$ s, giving:

$$\omega_\zeta = \frac{2\pi}{0.04} = 157.08 \text{ rad/s} \quad \checkmark$$

The natural frequency depends on $\lambda$:

$$\omega_0^2 = \frac{2G}{R_0^3}\left[\lambda - M_{\mathrm{enc}}\right]$$

For $\lambda = 1$ and $M_{\mathrm{enc}} \approx 1$ (order of magnitude), we get $\omega_0^2 \approx 0$, indicating the system is **near-critically balanced**, making it susceptible to secular drift.

When $\lambda < M_{\mathrm{enc}}$, we have $\omega_0^2 < 0$, yielding imaginary frequencies and exponential instability rather than oscillations.

---

## 4. Energy Analysis

### 4.1 Total Energy

The total energy of the system is:

$$E_{\mathrm{total}} = T + U_{\mathrm{grav}} + U_{\zeta}(t)$$

**Kinetic energy:**
$$T = \sum_{i=1}^N \frac{1}{2}m_i v_i^2$$

**Gravitational potential:**
$$U_{\mathrm{grav}} = -\frac{1}{2}\sum_{i \neq j} \frac{Gm_i m_j}{r_{ij}^2 + \epsilon_g^2}$$

**Repulsive potential:**
$$U_{\zeta}(t) = +\frac{1}{2}\sum_{i \neq j} \frac{\lambda G \zeta(t)}{r_{ij}^2 + \epsilon_\zeta^2}$$

### 4.2 Work Done Per Cycle

Since $\zeta(t)$ is time-dependent, the system is **non-conservative**. The work done by the repulsive force over one period $T = 2\pi/\omega_\zeta$ is:

$$W_{\mathrm{cycle}} = \oint \vec{F}_{\zeta}(t) \cdot d\vec{r}$$

For stable oscillations, we require:

$$W_{\mathrm{cycle}} \approx 0$$

Otherwise, energy accumulates and the system secularly expands or contracts.

### 4.3 Adiabatic Invariance Violation

The **adiabatic invariant** for a harmonic oscillator is:

$$I = \frac{E}{\omega_0}$$

When $\omega_\zeta \approx \omega_0$, the driving frequency matches the natural frequency, violating adiabatic invariance and causing **resonant energy pumping**.

---

## 5. Phase Space Analysis

### 5.1 Poincaré Sections

Consider the phase space $(R, \dot{R})$ sampled at phases $\omega_\zeta t = 2\pi n$ (stroboscopic map). For a perfectly periodic orbit:

$$R(t + T) = R(t), \quad \dot{R}(t + T) = \dot{R}(t)$$

The Poincaré section should show a **fixed point**.

### 5.2 Floquet Analysis

The linearized dynamics near equilibrium are described by the Floquet matrix:

$$\boldsymbol{\Phi}(t) = \begin{pmatrix} R(t) & \dot{R}(t) \\ \dot{R}(t) & \ddot{R}(t) \end{pmatrix}$$

Stability requires all Floquet multipliers $\mu_i$ satisfy $|\mu_i| \leq 1$. When $\lambda = 1$, the system sits near the **parametric resonance boundary**, where one multiplier approaches $|\mu| = 1$ from above, indicating marginal stability and secular drift.

---

## 6. Analytical Framework

### 6.1 Impedance Matching Argument

The effective "impedance" of gravitational contraction is:

$$Z_{\mathrm{grav}} \sim \frac{GM}{R_0^2}$$

The effective impedance of repulsive expansion (time-averaged) is:

$$Z_{\mathrm{rep}} \sim \frac{\lambda G \langle\zeta\rangle}{R_0^2} = \frac{\lambda G}{R_0^2}$$

For **equal impedance** (naive balance):
$$\lambda = M \approx 1$$

However, the **nonlinear response** of the system to oscillating forces means the effective coupling differs from the linear prediction.

### 6.2 Effective Force Scaling

The RMS force from modulation is:

$$F_{\mathrm{RMS}} = \frac{G\lambda}{R_0^2}\sqrt{\langle\zeta^2\rangle - \langle\zeta\rangle^2}$$

Since $\zeta(t) = 1 + \sin(\omega_\zeta t)$:

$$\langle\zeta^2\rangle = \left\langle(1 + \sin\theta)^2\right\rangle = 1 + 2\langle\sin\theta\rangle + \langle\sin^2\theta\rangle = 1 + 0 + \frac{1}{2} = \frac{3}{2}$$

$$F_{\mathrm{RMS}} = \frac{G\lambda}{R_0^2}\sqrt{\frac{3}{2} - 1} = \frac{G\lambda}{R_0^2} \cdot \frac{1}{\sqrt{2}}$$

The **time-averaged force magnitude** involves higher-order terms. A critical scaling factor $\lambda_{\mathrm{critical}}$ must account for:
1. Velocity-dependent orbital dynamics
2. Phase lag between force and displacement
3. Non-sinusoidal response to sinusoidal driving

### 6.3 Virial Theorem Considerations

The virial theorem for self-gravitating systems states:

$$2T + U = 0$$

For our system with time-varying forces:

$$2T(t) + U_{\mathrm{grav}} + U_{\zeta}(t) = 0$$

Time-averaging over one period:

$$2\langle T\rangle + \langle U_{\mathrm{grav}}\rangle + \lambda G\langle U'_{\zeta}\rangle = 0$$

where $U'_{\zeta}$ is the geometric part of the repulsive potential. Since $\langle\zeta(t)\rangle = 1$:

$$\lambda = -\frac{2\langle T\rangle + \langle U_{\mathrm{grav}}\rangle}{\langle U'_{\zeta}\rangle}$$

For a **stable breathing mode**, the virial balance must account for **pulsation energy**.

---

## 7. Parametric Resonance Theory

### 7.1 Mathieu Equation

The radial oscillation with time-varying effective "spring constant" is a **Mathieu equation**:

$$\ddot{R} + \left[\omega_0^2 + h\cos(\omega_\zeta t)\right]R = 0$$

where:
$$\omega_0^2 = \frac{2GM}{R_0^3}(\lambda - 1)$$
$$h = \frac{2G\lambda A}{R_0^3}$$

### 7.2 Stability Diagram

The Mathieu equation has **stability tongues** in the $(\omega_0^2, h)$ parameter space. Parametric resonance occurs when:

$$\omega_\zeta \approx 2\omega_0/n \quad (n = 1, 2, 3, \ldots)$$

For $\lambda = 1$: $\omega_0 \approx 0$, placing the system **near the principal instability tongue** (n=1).

For $\lambda > 1$: $\omega_0^2 > 0$, shifting away from resonance and enabling stable oscillations.

### 7.3 Critical Scaling Estimate

The boundary of the first instability tongue (approximately) depends on the modulation amplitude and system parameters. The critical value $\lambda_{\mathrm{crit}}$ must satisfy:

$$\omega_0^2 = \frac{2G}{R_0^3}(\lambda_{\mathrm{crit}} - M_{\mathrm{enc}}) \neq 0$$

to avoid the resonance condition.

---

## 8. Multi-Particle Corrections

### 8.1 Collective Mode Analysis

For $N = 100$ particles in a ring, the **breathing mode** is a collective oscillation where all particles move radially in phase:

$$\vec{r}_i(t) = \lambda(t) \vec{r}_i(0)$$

The mode frequency is determined by:

$$\ddot{\lambda} = -\frac{G M_{\mathrm{total}}}{\lambda^2 R_0^2} + \frac{\lambda G \zeta(t)}{\lambda^2 R_0^2}$$

This is **identical** to the single-particle equation, confirming the breathing mode is the dominant response.

### 8.2 Mode Coupling

Higher-order modes (quadrupole, hexapole, etc.) can couple to the breathing mode if $\lambda \neq \lambda_{\mathrm{crit}}$. This coupling extracts energy from coherent oscillation, causing:
- **Thermalization** (random motion)
- **Secular drift** (systematic expansion/contraction)

The critical value $\lambda_{\mathrm{crit}}$ **minimizes mode coupling**, maintaining coherent breathing.

---

## 9. Stability Conditions

### 9.1 Physical Interpretation

**$\lambda = 1.0$:**
- Time-averaged force balance, but **dynamic imbalance**
- System sits at parametric resonance boundary
- Small perturbations grow → secular expansion
- Energy pumped into system each cycle

**$\lambda > 1.0$:**
- Requires careful tuning to avoid resonance
- Natural frequency shifted away from driving frequency
- Potential for bounded oscillations
- Energy approximately conserved over cycles

**$\lambda < 1.0$:**
- $\omega_0^2 < 0$ yields imaginary frequencies
- Exponential instability dominates
- System collapses rather than oscillates

---

## 10. Generalization to Other Amplitudes

### 10.1 Scaling Law

For arbitrary modulation amplitude $A$, the critical scaling factor is expected to follow:

$$\lambda_{\mathrm{crit}}(A) \approx 1 + \beta A^2$$

where $\beta$ is a system-dependent constant that depends on the geometry, particle number, and softening parameters.

---

## 11. Conclusions

The stability of breathing oscillations in self-gravitating systems with time-varying repulsion depends critically on the scaling factor $\lambda$:

1. **Parametric resonance avoidance:** $\lambda = 1$ places the system at the boundary of Mathieu equation instability
2. **Nonlinear dynamics:** Time-averaged force balance (naive $\lambda = 1$) neglects velocity-dependent orbital effects
3. **Energy conservation:** Optimal $\lambda$ minimizes net work per cycle, preserving total energy
4. **Virial theorem modification:** Pulsating systems require correction to static virial balance
5. **Mode coupling suppression:** Off-resonance tuning prevents energy transfer to non-radial modes

The critical scaling factor represents a **dynamic equilibrium constant** that differs from the static force balance ratio due to the system's nonlinear response to time-varying forces.

---

## 12. Future Work

### 12.1 Recommended Investigations

1. **Amplitude scan:** Verify $\lambda_{\mathrm{crit}}(A)$ scaling law with $A \in [0.25, 1.5]$
2. **Energy tracking:** Implement diagnostic to measure $\Delta E_{\mathrm{cycle}}$ quantitatively
3. **Frequency scan:** Test stability for $\omega_\zeta \in [100, 200]$ rad/s
4. **Softening dependence:** Investigate how $\epsilon$ affects critical $\lambda$
5. **Multi-period evolution:** Run for $t = 10T$ to detect slow secular trends

### 12.2 Theoretical Extensions

1. Derive **exact critical $\lambda$** from Floquet analysis of Mathieu equation
2. Include **dissipative effects** (if numerical viscosity present)
3. Analyze **quasi-periodic orbits** for $\lambda \neq \lambda_{\mathrm{crit}}$
4. Extend to **3D geometry** (spherical shells)
5. Compare with **Jeans instability** in cosmological simulations

---

## References

1. McLachlan, N.W. (1947). *Theory and Application of Mathieu Functions*. Oxford University Press.
2. Landau, L.D. & Lifshitz, E.M. (1976). *Mechanics* (3rd ed.). Butterworth-Heinemann.
3. Goldstein, H., Poole, C., & Safko, J. (2002). *Classical Mechanics* (3rd ed.). Addison-Wesley.
4. Binney, J. & Tremaine, S. (2008). *Galactic Dynamics* (2nd ed.). Princeton University Press.
5. Nayfeh, A.H. & Mook, D.T. (1979). *Nonlinear Oscillations*. Wiley-Interscience.

---

**Document Version:** 1.1  
**Date:** 2024  
**Author:** Generated for GenericParticleSimulator project  
**License:** MIT