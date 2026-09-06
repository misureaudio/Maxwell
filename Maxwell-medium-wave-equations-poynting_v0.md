# Maxwell's Equations in a Medium: Wave Equations, the Poynting Vector, and Poynting's Theorem

This companion to *Maxwell-wave-equations-poynting* (vacuum) treats a material medium. The structure is the same: write the source equations, take curls to get wave equations, and build the energy balance. The new ingredients are the macroscopic fields $\mathbf{D},\mathbf{H}$, constitutive relations, free sources, and Ohmic loss.

---

## 1. Macroscopic Maxwell equations

In a material medium the microscopic fields are averaged over many atoms, introducing the **electric displacement** $\mathbf{D}$ and the **magnetic field intensity** $\mathbf{H}$. The source (macroscopic) equations are

$$\nabla \cdot \mathbf{D} = \rho_f$$

$$\nabla \cdot \mathbf{B} = 0$$

$$\nabla \times \mathbf{E} = -\,\frac{\partial \mathbf{B}}{\partial t}$$

$$\nabla \times \mathbf{H} = \mathbf{J}_f + \frac{\partial \mathbf{D}}{\partial t}$$

Here $\rho_f$ and $\mathbf{J}_f$ are the **free** (unbound) charge and current. The bound charge and magnetization of the material are absorbed into $\mathbf{D}$ and $\mathbf{H}$. Note:

- Gauss's law for magnetism is unchanged: there are no magnetic monopoles in any medium.
- Faraday's law is unchanged in form (the electric field is the same microscopic quantity).
- The two "source" laws are rewritten with $\mathbf{D},\mathbf{H}$ so that only free sources appear on the right.

---

## 2. Constitutive relations

For a **linear, isotropic, homogeneous** medium the response is proportional:

$$\mathbf{D} = \varepsilon\,\mathbf{E} = \varepsilon_0\varepsilon_r\,\mathbf{E}$$

$$\mathbf{B} = \mu\,\mathbf{H} = \mu_0\mu_r\,\mathbf{H}$$

$$\mathbf{J}_f = \sigma\,\mathbf{E} \qquad \text{(Ohmic conduction)}$$

where $\varepsilon_r$ is the relative permittivity, $\mu_r$ the relative permeability, and $\sigma$ the electrical conductivity. The limit $\varepsilon\to\varepsilon_0$, $\mu\to\mu_0$, $\sigma\to 0$ recovers vacuum.

Two limiting cases are developed below:

- **Case A — lossless dielectric:** $\sigma = 0$, $\rho_f = \mathbf{J}_f = 0$.
- **Case B — lossy (conducting) medium:** $\sigma \neq 0$, $\rho_f = 0$ (free charge in a conductor decays to the surface, so the bulk is neutral).

---

## 3. Case A — wave equation in a lossless dielectric

With $\sigma=0$ and no free sources, the equations are

$$\nabla\cdot\mathbf{E}=0, \qquad \nabla\cdot\mathbf{B}=0, \qquad \nabla\times\mathbf{E}=-\partial_t\mathbf{B}, \qquad \nabla\times\mathbf{H}=\partial_t\mathbf{D}$$

with $\mathbf{D}=\varepsilon\mathbf{E}$, $\mathbf{B}=\mu\mathbf{H}$.

### 3.1 Wave equation for $\mathbf{E}$

**Step 1 — Take the curl of Faraday's law:**

$$\nabla\times(\nabla\times\mathbf{E}) = -\,\frac{\partial}{\partial t}(\nabla\times\mathbf{H}) = -\,\frac{\partial}{\partial t}(\partial_t\mathbf{D}) = -\,\varepsilon\,\frac{\partial^2\mathbf{E}}{\partial t^2}$$

**Step 2 — Simplify the left-hand side** with the curl–curl identity. The divergence term vanishes because $\nabla\cdot\mathbf{E} = \nabla\cdot(\mathbf{D}/\varepsilon) = (\nabla\cdot\mathbf{D})/\varepsilon = 0$:

$$\nabla\times(\nabla\times\mathbf{E}) = \nabla(\nabla\cdot\mathbf{E}) - \nabla^2\mathbf{E} = -\,\nabla^2\mathbf{E}$$

**Step 3 — Equate:**

$$\boxed{\;\nabla^2\mathbf{E} = \varepsilon\mu\,\frac{\partial^2\mathbf{E}}{\partial t^2} = \frac{1}{v^2}\,\frac{\partial^2\mathbf{E}}{\partial t^2}\;}$$

### 3.2 Wave equation for $\mathbf{H}$

**Take the curl of the source-free Ampère law** $\nabla\times\mathbf{H}=\varepsilon\,\partial_t\mathbf{E}$:

$$\nabla\times(\nabla\times\mathbf{H}) = \varepsilon\,\frac{\partial}{\partial t}(\nabla\times\mathbf{E}) = \varepsilon\,\frac{\partial}{\partial t}(-\partial_t\mathbf{B}) = -\,\varepsilon\mu\,\frac{\partial^2\mathbf{H}}{\partial t^2}$$

The left-hand side is $-\nabla^2\mathbf{H}$ because $\nabla\cdot\mathbf{H} = (\nabla\cdot\mathbf{B})/\mu = 0$. Therefore

$$\boxed{\;\nabla^2\mathbf{H} = \frac{1}{v^2}\,\frac{\partial^2\mathbf{H}}{\partial t^2}\;}$$

### 3.3 Plane-wave consequences

With $\mathbf{E}=\mathbf{E}_0\,e^{i(\mathbf{k}\cdot\mathbf{x}-\omega t)}$ the wave equation gives $\omega = v\,|\mathbf{k}|$ with the **phase velocity**

$$\boxed{\;v = \frac{1}{\sqrt{\mu\varepsilon}} = \frac{c}{\sqrt{\mu_r\varepsilon_r}}\;}$$

and the **refractive index** $n = c/v = \sqrt{\mu_r\varepsilon_r}$ (for a non-magnetic medium $n\approx\sqrt{\varepsilon_r}$). Faraday's law gives

$$\mathbf{H} = \frac{\hat{\mathbf{k}}\times\mathbf{E}}{\eta}, \qquad \mathbf{B} = \frac{\hat{\mathbf{k}}\times\mathbf{E}}{v}$$

so the waves are again **transverse** ($\mathbf{E}\perp\mathbf{B}\perp\hat{\mathbf{k}}$), with $|\mathbf{B}| = |\mathbf{E}|/v$ (generalizing the vacuum $|\mathbf{B}|=|\mathbf{E}|/c$). The ratio $|\mathbf{E}|/|\mathbf{H}|$ is the **intrinsic (characteristic) impedance**

$$\boxed{\;\eta = \sqrt{\frac{\mu}{\varepsilon}} = \frac{\eta_0}{\sqrt{\mu_r\varepsilon_r}}, \qquad \eta_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}}\approx 377\ \Omega\;}$$

---

## 4. Case B — wave equation in a lossy (conducting) medium

Now $\mathbf{J}_f = \sigma\mathbf{E}$ but $\rho_f = 0$. The only equation that changes is Ampère's law:

$$\nabla\times\mathbf{H} = \sigma\mathbf{E} + \varepsilon\,\frac{\partial\mathbf{E}}{\partial t}$$

### 4.1 Damped wave equation

Take the curl of Faraday's law and substitute:

$$\nabla\times(\nabla\times\mathbf{E}) = -\,\frac{\partial}{\partial t}(\nabla\times\mathbf{H}) = -\,\frac{\partial}{\partial t}\Big(\sigma\mathbf{E}+\varepsilon\,\partial_t\mathbf{E}\Big) = -\,\sigma\mu\,\frac{\partial\mathbf{E}}{\partial t}-\,\varepsilon\mu\,\frac{\partial^2\mathbf{E}}{\partial t^2}$$

The left-hand side is still $-\nabla^2\mathbf{E}$ (since $\nabla\cdot\mathbf{E}=0$ in the neutral bulk). Hence

$$\boxed{\;\nabla^2\mathbf{E} = \varepsilon\mu\,\frac{\partial^2\mathbf{E}}{\partial t^2} + \sigma\mu\,\frac{\partial\mathbf{E}}{\partial t}\;}$$

This is the **damped (telegrapher's) wave equation**: the extra first-in-time term $\sigma\mu\,\partial_t\mathbf{E}$ damps the wave as it propagates. The same equation holds for $\mathbf{H}$.

### 4.2 Complex permittivity and complex wave number

For harmonic fields (time dependence $e^{-i\omega t}$, so $\partial_t\to -i\omega$) the equation becomes

$$\nabla^2\mathbf{E} + \omega^2\mu\Big(\varepsilon + i\frac{\sigma}{\omega}\Big)\mathbf{E} = 0$$

Define the **complex permittivity**

$$\varepsilon_c = \varepsilon + i\,\frac{\sigma}{\omega}$$

so that, for a plane wave $e^{i\mathbf{k}\cdot\mathbf{x}}$ (complex $\mathbf{k}$),

$$k^2 = \omega^2\mu\varepsilon_c = \omega^2\mu\varepsilon\Big(1 + i\,\frac{\sigma}{\omega\varepsilon}\Big)$$

Write $k = k_r + i k_i$ (propagation along $+x$): the real part $k_r$ sets the phase and the imaginary part $k_i$ sets the attenuation, $\mathbf{E}\propto e^{ik_r x}e^{-k_i x}e^{-i\omega t}$. Matching real and imaginary parts of $k^2$:

$$k_r^2 - k_i^2 = \omega^2\mu\varepsilon, \qquad 2k_r k_i = \omega\mu\sigma$$

The dimensionless ratio $\sigma/(\omega\varepsilon)$ is the **loss tangent** $\tan\delta_{\text{loss}}$.

### 4.3 Good conductor ($\sigma \gg \omega\varepsilon$)

Here $\omega^2\mu\varepsilon \ll \omega\mu\sigma$, so $k^2\approx i\omega\mu\sigma$ and

$$k \approx \sqrt{\frac{\omega\mu\sigma}{2}}\,(1+i), \qquad k_r \approx k_i \approx \sqrt{\frac{\omega\mu\sigma}{2}}$$

The field decays as $e^{-x/\delta}$ with the **skin depth**

$$\boxed{\;\delta = \frac{1}{k_i} = \sqrt{\frac{2}{\omega\mu\sigma}} = \sqrt{\frac{\rho}{\pi f\,\mu}}\;} \qquad (\rho = 1/\sigma)$$

The phase velocity is $v_p = \omega/k_r = \sqrt{2\omega/(\mu\sigma)}$, and the intrinsic impedance is $k_r\approx k_i$ giving $\eta \approx (1+i)\sqrt{\omega\mu\sigma/2}$: the field penetrates only a few skin depths, and $\mathbf{H}$ lags $\mathbf{E}$ by $45^\circ$.

### 4.4 Lossy dielectric ($\sigma \ll \omega\varepsilon$)

Here $k_r \gg k_i$, so

$$k_r \approx \omega\sqrt{\mu\varepsilon}, \qquad k_i \approx \frac{\sigma}{2}\sqrt{\frac{\mu}{\varepsilon}}$$

The wave travels almost at the lossless speed $v=1/\sqrt{\mu\varepsilon}$ but is weakly attenuated; the attenuation per unit length is $k_i$ (nepers/m).

---

## 5. Poynting's theorem and the Poynting vector in a medium

### 5.1 Derivation (general, valid for any medium + sources)

Use the two curl equations in macroscopic form:

$$\nabla\times\mathbf{E} = -\,\partial_t\mathbf{B}, \qquad \nabla\times\mathbf{H} = \mathbf{J}_f + \partial_t\mathbf{D}$$

Form $\mathbf{H}\cdot(\nabla\times\mathbf{E}) - \mathbf{E}\cdot(\nabla\times\mathbf{H})$ and apply the identity $\nabla\cdot(\mathbf{E}\times\mathbf{H}) = \mathbf{H}\cdot(\nabla\times\mathbf{E}) - \mathbf{E}\cdot(\nabla\times\mathbf{H})$:

$$\nabla\cdot(\mathbf{E}\times\mathbf{H}) = \mathbf{H}\cdot(-\partial_t\mathbf{B}) - \mathbf{E}\cdot(\mathbf{J}_f + \partial_t\mathbf{D}) = -\,\mathbf{H}\cdot\partial_t\mathbf{B} - \mathbf{E}\cdot\partial_t\mathbf{D} - \mathbf{E}\cdot\mathbf{J}_f$$

Rearranging,

$$\mathbf{E}\cdot\partial_t\mathbf{D} + \mathbf{H}\cdot\partial_t\mathbf{B} = -\,\nabla\cdot(\mathbf{E}\times\mathbf{H}) - \mathbf{E}\cdot\mathbf{J}_f$$

For a **linear, time-invariant, non-dispersive** medium ($\mathbf{D}=\varepsilon\mathbf{E}$, $\mathbf{B}=\mu\mathbf{H}$ with constant $\varepsilon,\mu$), the left-hand side is a total time derivative:

$$\mathbf{E}\cdot\partial_t\mathbf{D} = \partial_t\!\Big(\tfrac{1}{2}\varepsilon E^2\Big), \qquad \mathbf{H}\cdot\partial_t\mathbf{B} = \partial_t\!\Big(\tfrac{1}{2}\mu H^2\Big)$$

### 5.2 Energy density and Poynting vector

Define the **electromagnetic energy density** and the **Poynting vector** (the energy flux):

$$\boxed{\;u = \tfrac{1}{2}\,\mathbf{E}\cdot\mathbf{D} + \tfrac{1}{2}\,\mathbf{B}\cdot\mathbf{H} = \tfrac{1}{2}\,\varepsilon\,E^2 + \tfrac{1}{2}\,\mu\,H^2 = \tfrac{1}{2}\,\varepsilon\,E^2 + \tfrac{1}{2\mu}\,B^2\;}$$

$$\boxed{\;\mathbf{S} = \mathbf{E}\times\mathbf{H}\;} \qquad (\text{units: W/m}^2)$$

(These reduce to the vacuum expressions when $\varepsilon\to\varepsilon_0$, $\mu\to\mu_0$; note $\mathbf{S}=\tfrac{1}{\mu_0}\mathbf{E}\times\mathbf{B}$ in vacuum because $\mathbf{H}=\mathbf{B}/\mu_0$.)

### 5.3 Poynting's theorem

Substituting into the identity above gives the **differential form**

$$\boxed{\;\frac{\partial u}{\partial t} + \nabla\cdot\mathbf{S} = -\,\mathbf{E}\cdot\mathbf{J}_f\;}$$

Integrating over a volume $V$ bounded by a surface $S$ with outward normal:

$$\boxed{\;\frac{d}{dt}\int_V u\,dV = -\oint_S \mathbf{S}\cdot d\mathbf{a} \;-\; \int_V \mathbf{E}\cdot\mathbf{J}_f\,dV\;}$$

**Reading:** the rate of change of stored electromagnetic energy in $V$ equals (net power flowing *into* $V$ through its surface) minus (power dissipated inside $V$). This is the local statement of energy conservation for fields in a medium.

### 5.4 Ohmic (Joule) loss

For an Ohmic medium $\mathbf{J}_f = \sigma\mathbf{E}$, so

$$\mathbf{E}\cdot\mathbf{J}_f = \sigma\,E^2 \ge 0$$

is the **Joule heating density** (power per unit volume converted to heat). Special cases:

- **Lossless, source-free dielectric** ($\mathbf{J}_f=0$): $\partial_t u + \nabla\cdot\mathbf{S} = 0$ — exactly the vacuum continuity equation, with $u$ and $\mathbf{S}$ in the medium form.
- **Conductor**: part of the flux is steadily converted to heat, which is why the wave attenuates over the skin depth.

---

## 6. Intensity of a plane wave in a dielectric

For a monochromatic plane wave traveling along $\hat{\mathbf{k}}$ in a lossless dielectric, $\mathbf{H} = (\hat{\mathbf{k}}\times\mathbf{E})/\eta$, so

$$\mathbf{S} = \mathbf{E}\times\mathbf{H} = \frac{1}{\eta}\,\mathbf{E}\times\hat{\mathbf{k}}, \qquad |\mathbf{S}| = \frac{E^2}{\eta}$$

Time-averaging over a period for $\mathbf{E}=\mathbf{E}_0\cos(\mathbf{k}\cdot\mathbf{x}-\omega t)$ ($\langle\cos^2\rangle=\tfrac12$) gives the **intensity**

$$\boxed{\;I = \langle S\rangle = \frac{E_0^2}{2\,\eta} = \tfrac{1}{2}\,\varepsilon\, v\, E_0^2\;}$$

Compare with vacuum $I = E_0^2/(2\eta_0)$: a dielectric of index $n$ carries more intensity for the same field amplitude, since $\eta = \eta_0/n$ (non-magnetic case). In a **lossy** medium the intensity decays as $I(x) = I_0\,e^{-2k_i x}$ (the factor $2$ because $I\propto E^2$).

---

## 7. Caveats for general media

The clean wave equation and the simple energy density above assume a **linear, isotropic, homogeneous, non-dispersive** medium. Outside that class the picture changes:

- **Dispersive** ($\varepsilon=\varepsilon(\omega)$, $\mu=\mu(\omega)$): $\mathbf{E}\cdot\partial_t\mathbf{D}\neq\partial_t(\tfrac12\varepsilon E^2)$, so the stored energy is not simply $\tfrac12\varepsilon E^2$. For a single harmonic, $u = \tfrac12\frac{d(\omega\varepsilon)}{d\omega}E^2 + \tfrac12\frac{d(\omega\mu)}{d\omega}H^2$ (the Brillouin formula). The wave equation still holds but $k=k(\omega)$, so different frequencies travel at different speeds (pulse dispersion).
- **Anisotropic** ($\mathbf{D}=\boldsymbol{\varepsilon}\cdot\mathbf{E}$, $\boldsymbol{\varepsilon}$ a tensor): the $\nabla(\nabla\cdot\mathbf{E})$ term no longer decouples, the wave equation couples the field components, and the medium is birefringent (two polarization eigenmodes with different velocities).
- **Nonlinear** ($\mathbf{D}=\mathbf{D}(\mathbf{E})$): no linear wave equation; superposition fails, giving harmonic generation, self-focusing, etc.

---

## 8. Summary of results

| Quantity | Lossless dielectric | Vacuum (limit) |
|---|---|---|
| Wave equation | $\nabla^2\mathbf{F} = \mu\varepsilon\,\partial_t^2\mathbf{F} = \frac{1}{v^2}\partial_t^2\mathbf{F}$, $\mathbf{F}\in\{\mathbf{E},\mathbf{H}\}$ | same, $\mu=\mu_0$, $\varepsilon=\varepsilon_0$ |
| Phase velocity | $v = 1/\sqrt{\mu\varepsilon} = c/\sqrt{\mu_r\varepsilon_r}$ | $c = 1/\sqrt{\mu_0\varepsilon_0}$ |
| Refractive index | $n = c/v = \sqrt{\mu_r\varepsilon_r}$ | $1$ |
| Intrinsic impedance | $\eta = \sqrt{\mu/\varepsilon} = \eta_0/\sqrt{\mu_r\varepsilon_r}$ | $\eta_0\approx 377\ \Omega$ |
| Field ratio | $|\mathbf{B}| = |\mathbf{E}|/v$, $\;|\mathbf{E}|/|\mathbf{H}| = \eta$ | $|\mathbf{B}| = |\mathbf{E}|/c$ |
| Damped wave eq. (lossy) | $\nabla^2\mathbf{E} = \varepsilon\mu\,\partial_t^2\mathbf{E} + \sigma\mu\,\partial_t\mathbf{E}$ | — |
| Complex permittivity | $\varepsilon_c = \varepsilon + i\sigma/\omega$ | — |
| Skin depth (good conductor) | $\delta = \sqrt{2/(\omega\mu\sigma)} = \sqrt{\rho/(\pi f\mu)}$ | — |
| Energy density | $u = \tfrac12\varepsilon E^2 + \tfrac12\mu H^2$ | $u = \tfrac12\varepsilon_0 E^2 + \tfrac12\mu_0 H^2$ |
| Poynting vector | $\mathbf{S} = \mathbf{E}\times\mathbf{H}$ | $\mathbf{S} = \tfrac1{\mu_0}\mathbf{E}\times\mathbf{B}$ |
| Poynting's theorem | $\partial_t u + \nabla\cdot\mathbf{S} = -\mathbf{E}\cdot\mathbf{J}_f$ | $\partial_t u + \nabla\cdot\mathbf{S} = 0$ |
| Momentum density | $\mathbf{g} = \mathbf{S}/c^2 = \varepsilon\,\mathbf{E}\times\mathbf{H}$ (approx.) | $\mathbf{g} = \varepsilon_0\,\mathbf{E}\times\mathbf{B}$ |
| Intensity (plane wave) | $I = E_0^2/(2\eta) = \tfrac12\varepsilon v E_0^2$ | $I = E_0^2/(2\eta_0)$ |
