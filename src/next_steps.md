# PyParticleSim; Next Steps

**Current Status:** v0.1.0 - Core particle dynamics and structure generators complete

----------

## Immediate Development Plan

### 1. Force Field Implementation

**Goal:** Create `SK_Field` class for particle-particle interactions (will be renamed more appropriately later)

**Design:**

-   **Location:** New file `fields.py` (separate from `pyparticlesim.py`)
-   **Architecture:** Stateless field class that computes forces without mutating particles
-   **Class Template:**

```python
class SK_Field:
    def __init__(self, field_type='gravity', **params):
        self.field_type = field_type
        self.params = params  # e.g., G, epsilon, sigma
    
    def compute_forces(self, particles):
        """Return array of force vectors for each particle."""
        # N-body interactions or field calculations
        pass
```

-   **Usage Pattern:**

```python
field = SK_Field('lennard_jones', epsilon=1.0, sigma=1.0)
forces = field.compute_forces(particles)  # Returns array of [Fx, Fy]
```

**Forces to Implement:**

-   **Lennard-Jones:** $\vec{F} _{\mathrm{LJ}} = \frac{24\epsilon}{r}\left[2\left(\frac{\sigma}{r}\right)^{13} - \left(\frac{\sigma}{r}\right)^7\right]\hat{r}$
-   **N-body Gravitational:** $\vec{F} _{\mathrm{grav}} = -\frac{Gm _1m _2}{r^2}\hat{r}$

**Key Requirements:**

-   Return force arrays, don't mutate `Particle` objects directly
-   Preserve force accumulator pattern in `Particle.apply_forces()`
-   $O(N^2)$ pairwise interactions using double loop
-   Integration with `Simulation.step(*force_funcs)` workflow

----------

### 2. Trajectory Recording

**Goal:** Track particle positions over time for analysis and visualization

**Implementation:**

-   Add optional recording to `Simulation` class
-   Store timestamped position arrays: `[(t, positions), ...]`
-   Design decision: Store in `Simulation` instance or return from `run()`?

**Considerations:**

-   Memory usage for long simulations
-   Data structure: list of arrays vs. pre-allocated 3D array
-   Access pattern for animation tool

----------

### 3. Animation Tool

**Goal:** Visualize particle dynamics from recorded trajectories

**Approach:**

-   Use `matplotlib.animation.FuncAnimation`
-   Input: trajectory data from step 2
-   Output: animated scatter plot or saved video (MP4/GIF)

**Features:**

-   Adjustable playback speed
-   Optional particle trails
-   Axis scaling (equal aspect ratio for physical accuracy)

----------

## Testing Strategy

**Before expanding package:**

1.  Visualize initial particle structures with matplotlib scatter plots
2.  Run short simulations and print before/after positions
3.  Validate physics with analytical solutions (circular orbits, oscillators)
4.  Create simple animations to verify force implementations

**Test cases:**

-   Gravitational collapse of particle cloud
-   LJ equilibration (particles finding energy minimum)
-   Combined forces (gravity + repulsion)

----------

## Design Principles

-   **Modularity:** Forces in separate module, maintains clean separation
-   **Reusability:** `SK_Field` stateless and generic across particle systems
-   **Compatibility:** New features integrate with existing force accumulator pattern
-   **Validation first:** Test physics before adding complexity

----------

## Future Considerations (Post-Visualization)

-   Verlet/RK4 integration methods
-   Energy/momentum diagnostics
-   Boundary conditions
-   Collision detection
-   Spatial partitioning for $O(N \log N)$ force calculations

----------

**Priority:** Implement → Record → Visualize → Validate → Iterate
