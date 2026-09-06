# Maxwell's Equations in Vacuum: Derivation of the Wave Equations and the Poynting Vector

## 1. Starting point

In vacuum there are no sources: $\rho = 0$ and $\mathbf{J} = 0$. Maxwell's equations in differential form reduce to

$$\nabla \cdot \mathbf{E} = 0$$

$$\nabla \cdot \mathbf{B} = 0$$

$$\nabla \times \mathbf{E} = -\,\frac{\partial \mathbf{B}}{\partial t}$$

$$\nabla \times \mathbf{B} = \mu_0\varepsilon_0\,\frac{\partial \mathbf{E}}{\partial t}$$

or, using $c^2 = 1/(\mu_0\varepsilon_0)$,

$$\nabla \times \mathbf{B} = \frac{1}{c^2}\,\frac{\partial \mathbf{E}}{\partial t}$$

The four equations are, respectively:

- **Gauss (electric):** no free charge, so $\mathbf{E}$ is divergence-free.
- **Gauss (magnetic):** no magnetic monopoles, so $\mathbf{B}$ is divergence-free (always true).
- **Faraday's law:** a time-varying $\mathbf{B}$ induces a circulating $\mathbf{E}$.
- **Ampère–Maxwell's law:** in vacuum the displacement current $\mu_0\varepsilon_0\,\partial_t \mathbf{E}$ is the only source of a circulating $\mathbf{B}$ (there is no conduction current).

Two vector identities are used in what follows:

$$\nabla \times (\nabla \times \mathbf{F}) = \nabla(\nabla \cdot \mathbf{F}) - \nabla^2 \mathbf{F}$$

$$\nabla \cdot (\mathbf{E} \times \mathbf{B}) = \mathbf{B} \cdot (\nabla \times \mathbf{E}) - \mathbf{E} \cdot (\nabla \times \mathbf{B})$$

---

## 2. Wave equation for $\mathbf{E}$

**Step 1 — Take the curl of Faraday's law.** The curl and the time derivative commute (the fields are assumed smooth):

$$\nabla \times (\nabla \times \mathbf{E}) = -\,\frac{\partial}{\partial t} (\nabla \times \mathbf{B})$$

**Step 2 — Simplify the left-hand side** with the curl–curl identity. The divergence term vanishes by Gauss's law in vacuum ($\nabla \cdot \mathbf{E} = 0$):

$$\nabla \times (\nabla \times \mathbf{E}) = \nabla(\nabla \cdot \mathbf{E}) - \nabla^2 \mathbf{E} = -\,\nabla^2 \mathbf{E}$$

**Step 3 — Substitute Ampère–Maxwell's law on the right-hand side:**

$$-\,\frac{\partial}{\partial t}(\nabla \times \mathbf{B}) = -\,\mu_0\varepsilon_0\,\frac{\partial^2 \mathbf{E}}{\partial t^2}$$

**Step 4 — Equate and rearrange:**

$$\boxed{\;\nabla^2 \mathbf{E} = \mu_0\varepsilon_0\,\frac{\partial^2 \mathbf{E}}{\partial t^2} = \frac{1}{c^2}\,\frac{\partial^2 \mathbf{E}}{\partial t^2}\;}$$

with $c^2 = 1/(\mu_0\varepsilon_0)$. This is the wave equation written componentwise: each of $E_x, E_y, E_z$ satisfies the same scalar wave equation.

---

## 3. Wave equation for $\mathbf{B}$

The argument is the mirror image. **Take the curl of Ampère–Maxwell's law:**

$$\nabla \times (\nabla \times \mathbf{B}) = \mu_0\varepsilon_0\,\frac{\partial}{\partial t}(\nabla \times \mathbf{E})$$

Left-hand side: $-\nabla^2 \mathbf{B}$, by the curl–curl identity and Gauss's law for magnetism ($\nabla \cdot \mathbf{B} = 0$).

Right-hand side: use Faraday's law, $\nabla \times \mathbf{E} = -\partial_t \mathbf{B}$:

$$\mu_0\varepsilon_0\,\frac{\partial}{\partial t}\!\left(-\frac{\partial \mathbf{B}}{\partial t}\right) = -\,\mu_0\varepsilon_0\,\frac{\partial^2 \mathbf{B}}{\partial t^2}$$

Therefore:

$$\boxed{\;\nabla^2 \mathbf{B} = \frac{1}{c^2}\,\frac{\partial^2 \mathbf{B}}{\partial t^2}\;}$$

---

## 4. Consequences: plane waves

Insert a monochromatic ansatz

$$\mathbf{E} = \mathbf{E}_0\, e^{i(\mathbf{k}\cdot\mathbf{x} - \omega t)}$$

into the wave equation: $\nabla^2 \mathbf{E} \to -k^2 \mathbf{E}$ and $\partial_t^2 \mathbf{E} \to -\omega^2 \mathbf{E}$, giving the dispersion relation

$$\omega = c\,|\mathbf{k}|$$

Faraday's law then gives

$$\mathbf{B}_0 = \frac{\hat{\mathbf{k}} \times \mathbf{E}_0}{c}$$

and $\nabla \cdot \mathbf{E} = 0$ gives $\mathbf{k}\cdot\mathbf{E}_0 = 0$. Hence the waves are **transverse**: they propagate at speed $c$, with $\mathbf{E} \perp \mathbf{B} \perp \hat{\mathbf{k}}$ and $|\mathbf{B}_0| = |\mathbf{E}_0|/c$.

---

## 5. The Poynting vector

**Step 1 — Energy density.** The vacuum electromagnetic energy density is the sum of the electric and magnetic contributions:

$$u = \tfrac{1}{2}\,\varepsilon_0\, E^2 + \tfrac{1}{2\mu_0}\, B^2$$

**Step 2 — Differentiate in time:**

$$\frac{\partial u}{\partial t} = \varepsilon_0\,\mathbf{E}\cdot\frac{\partial \mathbf{E}}{\partial t} + \frac{1}{\mu_0}\,\mathbf{B}\cdot\frac{\partial \mathbf{B}}{\partial t}$$

**Step 3 — Replace the time derivatives with curls.** From Ampère–Maxwell's law, $\partial_t \mathbf{E} = \frac{1}{\mu_0\varepsilon_0}\nabla\times\mathbf{B}$; from Faraday's law, $\partial_t \mathbf{B} = -\nabla\times\mathbf{E}$:

$$\frac{\partial u}{\partial t} = \frac{1}{\mu_0}\,\mathbf{E}\cdot(\nabla\times\mathbf{B}) \;-\; \frac{1}{\mu_0}\,\mathbf{B}\cdot(\nabla\times\mathbf{E})$$

**Step 4 — Recognize the divergence identity** $\nabla\cdot(\mathbf{E}\times\mathbf{B}) = \mathbf{B}\cdot(\nabla\times\mathbf{E}) - \mathbf{E}\cdot(\nabla\times\mathbf{B})$:

$$\frac{\partial u}{\partial t} = -\,\nabla\cdot\!\left(\frac{\mathbf{E}\times\mathbf{B}}{\mu_0}\right)$$

**Step 5 — Read off the continuity equation.** This is $\partial_t u + \nabla\cdot\mathbf{S} = 0$ — local conservation of energy with no sources or sinks — where the flux is the **Poynting vector**:

$$\boxed{\;\mathbf{S} = \frac{1}{\mu_0}\,\mathbf{E}\times\mathbf{B}\;} \qquad (\text{units: W/m}^2)$$

Interpretation: $\mathbf{S}$ is the energy flux — the rate at which electromagnetic energy crosses a unit area, flowing in the direction of $\mathbf{E}\times\mathbf{B}$.

---

## 6. Intensity of a plane wave

For a monochromatic plane wave traveling along $\hat{\mathbf{k}}$, one has $\mathbf{B} = (\hat{\mathbf{k}}\times\mathbf{E})/c$, so

$$\mathbf{S} = \frac{1}{\mu_0}\,\mathbf{E}\times\mathbf{B} = \frac{1}{\mu_0 c}\,\mathbf{E}\times\hat{\mathbf{k}}$$

and therefore $|\mathbf{S}| = E^2/(\mu_0 c)$, pointing along $\hat{\mathbf{k}}$. Time-averaging over a period for $\mathbf{E} = \mathbf{E}_0\cos(\mathbf{k}\cdot\mathbf{x}-\omega t)$, using $\langle\cos^2\rangle = \tfrac12$, gives the **intensity**:

$$I = \langle S \rangle = \frac{E_0^2}{2\,\mu_0 c} = \frac{1}{2}\,\varepsilon_0 c\, E_0^2$$

As a bonus, the same algebra shows that $\mathbf{S}/c^2 = \varepsilon_0\,\mathbf{E}\times\mathbf{B}$ is the electromagnetic **momentum density**: light carries momentum as well as energy.

---

## 7. Summary of results

| Quantity | Expression |
|---|---|
| Wave equation (both fields) | $\nabla^2 \mathbf{F} = \frac{1}{c^2}\frac{\partial^2 \mathbf{F}}{\partial t^2}$, $\;\mathbf{F} \in \{\mathbf{E}, \mathbf{B}\}$ |
| Speed of propagation | $c = 1/\sqrt{\mu_0\varepsilon_0}$ |
| Dispersion relation | $\omega = c\,|\mathbf{k}|$ |
| Energy density | $u = \tfrac{1}{2}\varepsilon_0 E^2 + \tfrac{1}{2\mu_0}B^2$ |
| Poynting vector | $\mathbf{S} = \frac{1}{\mu_0}\mathbf{E}\times\mathbf{B}$ |
| Energy conservation | $\partial_t u + \nabla\cdot\mathbf{S} = 0$ |
| Momentum density | $\mathbf{g} = \mathbf{S}/c^2 = \varepsilon_0\,\mathbf{E}\times\mathbf{B}$ |
| Intensity (monochromatic plane wave) | $I = E_0^2/(2\mu_0 c) = \tfrac{1}{2}\varepsilon_0 c\,E_0^2$ |
