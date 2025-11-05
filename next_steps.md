# PyParticleSim: Next Steps

**Last Updated:** November 5, 2025

---

## Code Development Priorities

### 1. Trajectory Recording System
**Status:** Not started  
**Goal:** Track particle positions over time for analysis and visualization

**Implementation:**
- Add trajectory storage to `Verlet_Simulation` and `User_Simulation` classes
- Store timestamped position arrays: `[(t, positions), ...]`
- Design decision needed: Store in simulation instance vs. return from `run()`
- Consider memory efficiency for long simulations

**Deliverable:** Method to extract full trajectory history after simulation completes

---

### 2. Animation Tool
**Status:** Not started  
**Goal:** Visualize particle dynamics from recorded trajectories

**Approach:**
- Use `matplotlib.animation.FuncAnimation`
- Input: trajectory data from Priority 1
- Output: animated scatter plot or saved video (MP4/GIF)

**Features:**
- Adjustable playback speed
- Optional particle trails
- Equal aspect ratio for physical accuracy

**Deliverable:** Standalone animation script that takes trajectory data as input

---

### 3. Testing and Validation
**Status:** Ongoing

**Test cases needed:**
- Gravitational collapse with circle vs square geometries
- Energy conservation verification (track total energy over time)
- Long-term stability comparison (Euler vs Verlet at t > 0.5)

---

## Paper Development Priorities

### 1. Fix Conclusion on Pattern Persistence
**Status:** Critical revision needed  
**Issue:** Current text implies Verlet patterns persist indefinitely

**Required changes:**
- Acknowledge both methods eventually lead to gravitational singularity
- Clarify Verlet maintains structure *longer* than Euler, not indefinitely
- Explain that organized patterns are transient, not permanent equilibria
- Revise abstract and Section 3.1 to reflect this understanding

**Key point:** Verlet degrades gracefully toward physical collapse; Euler exhibits rapid artificial collapse

---

### 2. Add Circle Geometry Results
**Status:** Not started  
**Goal:** Demonstrate method comparison is geometry-independent

**Required simulations:**
- Circle initial configuration with same parameters as square tests
- Both Euler and Verlet at t=0.1 (matching Figure 3.1 conditions)
- Parameters: G=10, ε=0.05, Δt=10⁻⁵, n_steps=10⁴

**Deliverable:**
- New figure showing circle collapse comparison
- Brief discussion in Section 3.1 confirming geometry-independence
- Update abstract if results are noteworthy

---

### 3. Expand Scientific Context
**Status:** In progress  
**Areas needing additional content:**

**Section 1 (Euler):**
- Add brief discussion of when Euler *is* appropriate (non-stiff, short-time)
- Quantify "stiff dynamics" more precisely (characteristic timescales)

**Section 2 (Systematic Errors):**
- Already strong, minimal additions needed

**Section 3 (Verlet):**
- Explain phase space preservation more intuitively (before Appendix reference)
- Add physical interpretation of "bounded energy errors"
- Discuss computational cost tradeoff (2× force evaluations)

**New subsection candidates:**
- Energy tracking plots (E vs t for both methods)
- Quantitative stiffness analysis (dynamical timescale calculations)

---

### 4. Write Introduction and Conclusion
**Status:** Not started

**Introduction requirements:**
- Motivation: Why N-body simulations matter (astrophysics, molecular dynamics)
- Problem statement: Energy conservation challenges in long-term integration
- Preview of findings: Symplectic methods essential for conservative systems
- Paper structure overview
- Length: 1-1.5 pages

**Conclusion requirements:**
- Restate key finding: Verlet preserves structure longer than Euler
- Acknowledge limitations: Both eventually collapse, timestep constraints remain
- Practical recommendations: When to use each method
- Future work: Adaptive timesteps, implicit methods, higher-order symplectic integrators
- Length: 0.75-1 page

---

## Timeline Estimates

**Code priorities:**
- Trajectory recording: 2-3 hours
- Animation tool: 3-4 hours
- Circle simulations: 1 hour

**Paper priorities:**
- Fix conclusion: 1 hour
- Circle results section: 2 hours (after simulations complete)
- Expand science: 3-4 hours
- Intro + conclusion: 4-5 hours

**Total estimated effort:** 16-22 hours

---

## Dependencies

- Paper Priority 2 (circle results) depends on Code Priority 2 (trajectory recording) for visualization
- Paper Priority 4 (intro/conclusion) should be written last, after all technical sections finalized
- Paper Priority 1 (fix conclusion) can proceed immediately

---

## Notes

- Maintain LaTeX formatting conventions from `latex_instructions.md`
- All simulations use PyParticleSim v0.1.0+ with Verlet_Simulation class
- Paper target length: 8-12 pages including appendices
- Consider energy conservation plots as strongest quantitative evidence for Verlet superiority
