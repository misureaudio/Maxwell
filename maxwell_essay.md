# Electromagnetic Waves: From Maxwell's Equations to Energy Transport in Matter

*Every equation in this essay was verified symbolically with SymPy (1.14.0); the verification scripts are provided alongside this document.*

---

## 1. Maxwell's equations in vacuum

In vacuum there are no sources — no free charge density $\rho$ and no current density $\mathbf{J}$ — and Maxwell's equations take their simplest, fully symmetric form. In differential form:

$$\nabla \cdot \mathbf{E} = 0 \tag{1}$$

$$\nabla \cdot \mathbf{B} = 0 \tag{2}$$

$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} \tag{3}$$

$$\nabla \times \mathbf{B} = \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t} \tag{4}$$

Here $\mathbf{E}$ and $\mathbf{B}$ are the electric and magnetic fields, $\varepsilon_0$ is the vacuum permittivity, and $\mu_0$ is the vacuum permeability. The four equations have a clean physical reading:

- **(1) Gauss's law for electricity (source-free).** The absence of charge means electric field lines have no beginning or end in empty space; the flux of $\mathbf{E}$ through any closed surface vanishes.
- **(2) Gauss's law for magnetism.** There are no magnetic monopoles; magnetic field lines always close on themselves.
- **(3) Faraday's law.** A time-varying magnetic field induces a circulating electric field.
- **(4) The Ampère–Maxwell law.** A time-varying electric field (the displacement current) induces a circulating magnetic field.

The last two equations are the engine of the whole theory: a changing $\mathbf{B}$ creates $\mathbf{E}$, and a changing $\mathbf{E}$ creates $\mathbf{B}$. That mutual induction is what makes self-sustaining electromagnetic waves possible.

Two constants are already hiding in these equations. Their product

$$\mu_0 \varepsilon_0 = \frac{1}{c^2}$$

defines a speed $c = 1/\sqrt{\mu_0\varepsilon_0} \approx 3\times 10^8$ m/s. As the next section shows, this is not a coincidence: it is the speed at which the equations force any electromagnetic disturbance to propagate.

---

## 2. The wave equation

The wave equations for $\mathbf{E}$ and $\mathbf{B}$ follow by one curl and one substitution each.

**Derivation for $\mathbf{E}$.** Take the curl of Faraday's law (3):

$$\nabla \times (\nabla \times \mathbf{E}) = \nabla \times \left(-\frac{\partial \mathbf{B}}{\partial t}\right).$$

Apply the vector identity $\nabla \times (\nabla \times \mathbf{E}) = \nabla(\nabla \cdot \mathbf{E}) - \nabla^2\mathbf{E}$ on the left, and interchange the curl and the time derivative on the right (they commute for smooth fields):

$$\nabla(\nabla \cdot \mathbf{E}) - \nabla^2\mathbf{E} = -\frac{\partial}{\partial t}(\nabla \times \mathbf{B}).$$

Now the two source-free Gauss laws do their work. By (1), $\nabla \cdot \mathbf{E} = 0$, so the first term vanishes. Substituting the Ampère–Maxwell law (4) for $\nabla \times \mathbf{B}$:

$$-\nabla^2\mathbf{E} = -\frac{\partial}{\partial t}\left(\mu_0\varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}\right).$$

Since $\mu_0\varepsilon_0$ is a constant it comes out of the derivative, and cancelling the minus signs gives

$$\boxed{\nabla^2\mathbf{E} = \frac{1}{c^2}\frac{\partial^2\mathbf{E}}{\partial t^2}.} \tag{5}$$

**Derivation for $\mathbf{B}$.** Symmetrically, take the curl of (4), use the vector identity with $\mathbf{B}$, drop the $\nabla(\nabla\cdot\mathbf{B})$ term via (2), and substitute Faraday's law (3) for $\nabla\times\mathbf{E}$:

$$-\nabla^2\mathbf{B} = \mu_0\varepsilon_0\frac{\partial}{\partial t}\left(-\frac{\partial\mathbf{B}}{\partial t}\right)
\quad\Longrightarrow\quad
\boxed{\nabla^2\mathbf{B} = \frac{1}{c^2}\frac{\partial^2\mathbf{B}}{\partial t^2}.} \tag{6}$$

**What this means.** Both fields independently satisfy the standard wave equation in three dimensions, propagating at speed

$$c = \frac{1}{\sqrt{\mu_0\varepsilon_0}} \approx 2.998\times 10^8\ \text{m/s}.$$

Equations (5)–(6) are the mathematical statement that a self-sustaining disturbance in $\mathbf{E}$ induces one in $\mathbf{B}$, and vice versa, and that this coupled disturbance travels through empty space at $c$. The identification of this $c$ with the measured speed of light is the content of Maxwell's great unification: light *is* an electromagnetic wave.

---

## 3. The plane-wave solution

Because the vacuum equations are linear with constant coefficients, the natural building blocks are monochromatic plane waves. We take the ansatz

$$\mathbf{E}(\mathbf{r},t) = \mathbf{E}_0\, e^{i(\mathbf{k}\cdot\mathbf{r} - \omega t)}, \qquad
\mathbf{B}(\mathbf{r},t) = \mathbf{B}_0\, e^{i(\mathbf{k}\cdot\mathbf{r} - \omega t)},$$

with constant (possibly complex) amplitudes $\mathbf{E}_0, \mathbf{B}_0$; the physical fields are the real parts. Each differential operator acts as a simple multiplication once the common factor $f = e^{i(\mathbf{k}\cdot\mathbf{r}-\omega t)}$ is stripped off:

| Equation | Result | Condition |
|---|---|---|
| $\nabla\cdot\mathbf{E}=0$ | $i\,\mathbf{k}\cdot\mathbf{E}_0 = 0$ | $\mathbf{k}\cdot\mathbf{E}_0 = 0$ |
| $\nabla\cdot\mathbf{B}=0$ | $i\,\mathbf{k}\cdot\mathbf{B}_0 = 0$ | $\mathbf{k}\cdot\mathbf{B}_0 = 0$ |
| $\nabla\times\mathbf{E}=-\partial_t\mathbf{B}$ | $i\,\mathbf{k}\times\mathbf{E}_0 = i\omega\mathbf{B}_0$ | $\mathbf{B}_0 = \dfrac{\mathbf{k}\times\mathbf{E}_0}{\omega}$ |
| $\nabla\times\mathbf{B}=\mu_0\varepsilon_0\,\partial_t\mathbf{E}$ | $i\,\mathbf{k}\times\mathbf{B}_0 = -i\mu_0\varepsilon_0\omega\mathbf{E}_0$ | $\mathbf{k}\times\mathbf{B}_0 = -\mu_0\varepsilon_0\omega\mathbf{E}_0$ |

### 3.1 The dispersion relation

Substituting $\mathbf{B}_0 = \mathbf{k}\times\mathbf{E}_0/\omega$ into the Ampère condition gives

$$\mathbf{k}\times(\mathbf{k}\times\mathbf{E}_0) = -\mu_0\varepsilon_0\omega^2\,\mathbf{E}_0.$$

The vector triple product $\mathbf{k}\times(\mathbf{k}\times\mathbf{E}_0) = \mathbf{k}(\mathbf{k}\cdot\mathbf{E}_0) - k^2\mathbf{E}_0$ yields

$$\mathbf{k}(\mathbf{k}\cdot\mathbf{E}_0) + \left(\mu_0\varepsilon_0\omega^2 - k^2\right)\mathbf{E}_0 = 0.$$

Dotting with $\mathbf{E}_0$ and using the transversality $\mathbf{k}\cdot\mathbf{E}_0 = 0$ leaves

$$\left(\mu_0\varepsilon_0\omega^2 - k^2\right)|\mathbf{E}_0|^2 = 0.$$

For a nontrivial wave ($\mathbf{E}_0 \neq 0$),

$$\boxed{\omega = c\,|\mathbf{k}|, \qquad c = \frac{1}{\sqrt{\mu_0\varepsilon_0}}.} \tag{7}$$

This is precisely the dispersion relation of the wave equation (5)–(6), confirming that the plane-wave ansatz is consistent with the PDE.

### 3.2 Polarization structure

All the geometric facts about plane waves follow from the single relation $\mathbf{B}_0 = \mathbf{k}\times\mathbf{E}_0/\omega$:

- **Transversality.** $\mathbf{k}\cdot\mathbf{E}_0 = 0$ by Gauss's law. For $\mathbf{B}_0$:
$$\mathbf{k}\cdot\mathbf{B}_0 = \frac{\mathbf{k}\cdot(\mathbf{k}\times\mathbf{E}_0)}{\omega} \equiv 0,$$
a scalar triple product with a repeated vector. Gauss's law for magnetism is satisfied automatically.
- **Orthogonality of $\mathbf{E}$ and $\mathbf{B}$.**
$$\mathbf{E}_0\cdot\mathbf{B}_0 = \frac{1}{\omega}\,\mathbf{E}_0\cdot(\mathbf{k}\times\mathbf{E}_0) = 0,$$
again a repeated vector in a triple product.
- **Amplitude ratio.** Since $\mathbf{E}_0 \perp \mathbf{k}$,
$$|\mathbf{B}_0| = \frac{k|\mathbf{E}_0|}{\omega} = \frac{|\mathbf{E}_0|}{c}.$$

The three vectors $\mathbf{E}_0$, $\mathbf{B}_0$, and $\hat{\mathbf{k}}$ therefore form a mutually orthogonal, right-handed triad with $\mathbf{B}_0 = \frac{1}{c}\,\hat{\mathbf{k}}\times\mathbf{E}_0$. In particular $\mathbf{E}\times\mathbf{B}$ points along $\hat{\mathbf{k}}$ — the direction of propagation. (The direction of propagation of the *energy* is confirmed a posteriori by the Poynting vector in §4.)

### 3.3 Explicit real solutions

Writing $\varphi = \mathbf{k}\cdot\mathbf{r} - \omega t$:

$$\mathbf{E} = \operatorname{Re}\!\left[\mathbf{E}_0 e^{i\varphi}\right] = \Re(\mathbf{E}_0)\cos\varphi - \Im(\mathbf{E}_0)\sin\varphi.$$

- **Linear polarization** ($\mathbf{E}_0$ real): $\mathbf{E} = \mathbf{E}_0\cos\varphi$; the field oscillates along a fixed direction.
- **Circular polarization** (e.g. $\mathbf{E}_0 = \tfrac{E_0}{\sqrt{2}}(\hat{x} + i\hat{y})$ for $\mathbf{k} = k\hat{z}$):
$$\mathbf{E} = \frac{E_0}{\sqrt{2}}\left(\hat{x}\cos\varphi - \hat{y}\sin\varphi\right),$$
a vector of constant magnitude rotating at angular frequency $\omega$.

### 3.4 A verified example

With $\mathbf{k} = k\hat{z}$, $\mathbf{E}_0 = E_x\hat{x}$, and $\omega = ck$, the relation $\mathbf{B}_0 = \hat{\mathbf{k}}\times\mathbf{E}_0/c$ gives $\mathbf{B}_0 = \frac{E_x}{c}\hat{y}$. Substituting this pair back into all four Maxwell equations (done symbolically with SymPy) yields exactly zero for each:

$$\nabla\cdot\mathbf{E} = 0,\quad \nabla\cdot\mathbf{B} = 0,\quad \nabla\times\mathbf{E} + \partial_t\mathbf{B} = \mathbf{0},\quad \nabla\times\mathbf{B} - \mu_0\varepsilon_0\,\partial_t\mathbf{E} = \mathbf{0},$$

and $\mathbf{E}\times\mathbf{B} \propto +\hat{z}$, confirming propagation along $\hat{\mathbf{k}}$.

Finally, linearity implies that any superposition

$$\mathbf{E}(\mathbf{r},t) = \int \tilde{\mathbf{E}}_0(\mathbf{k})\, e^{i(\mathbf{k}\cdot\mathbf{r} - c|\mathbf{k}|t)}\, d^3k$$

is also a solution — which is why arbitrary initial data can be built from plane waves.

---

## 4. Energy density and the Poynting vector in vacuum

The conservation law for electromagnetic energy is **Poynting's theorem**, derived as follows.

### 4.1 Derivation

From the Ampère–Maxwell law,

$$\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}
\quad\Longrightarrow\quad
\mathbf{J} = \frac{1}{\mu_0}\left(\nabla\times\mathbf{B} - \mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}\right).$$

The power per unit volume delivered by the fields to the charges is $\mathbf{J}\cdot\mathbf{E}$:

$$\mathbf{J}\cdot\mathbf{E} = \frac{1}{\mu_0}(\nabla\times\mathbf{B})\cdot\mathbf{E} - \varepsilon_0\,\mathbf{E}\cdot\frac{\partial\mathbf{E}}{\partial t}.$$

The key vector identity (verified term-by-term symbolically),

$$(\nabla\times\mathbf{B})\cdot\mathbf{E} = \nabla\cdot(\mathbf{E}\times\mathbf{B}) + (\nabla\times\mathbf{E})\cdot\mathbf{B},$$

rearranges this to

$$\mathbf{J}\cdot\mathbf{E} = \frac{1}{\mu_0}\nabla\cdot(\mathbf{E}\times\mathbf{B}) + \frac{1}{\mu_0}(\nabla\times\mathbf{E})\cdot\mathbf{B} - \varepsilon_0\,\mathbf{E}\cdot\frac{\partial\mathbf{E}}{\partial t}.$$

Faraday's law, $\nabla\times\mathbf{E} = -\partial_t\mathbf{B}$, together with the elementary "half trick" $\mathbf{E}\cdot\partial_t\mathbf{E} = \tfrac{1}{2}\partial_t E^2$ (and its magnetic analogue) gives

$$\mathbf{J}\cdot\mathbf{E} = \frac{1}{\mu_0}\nabla\cdot(\mathbf{E}\times\mathbf{B}) - \frac{\partial}{\partial t}\left[\frac{\varepsilon_0}{2}E^2 + \frac{1}{2\mu_0}B^2\right].$$

Rearranging into conservation-law form:

$$\boxed{\frac{\partial u}{\partial t} + \nabla\cdot\mathbf{S} = -\mathbf{J}\cdot\mathbf{E}, \qquad
u = \frac{\varepsilon_0}{2}|\mathbf{E}|^2 + \frac{1}{2\mu_0}|\mathbf{B}|^2, \qquad
\mathbf{S} \equiv \frac{1}{\mu_0}\,\mathbf{E}\times\mathbf{B}.} \tag{8}$$

**Reading (8).** $u$ is the electromagnetic energy density — half stored in the electric field, half in the magnetic. $\mathbf{S}$, the **Poynting vector**, is the energy flux (in W/m²). The statement: the change of field energy in a volume plus the net flux through its surface equals the energy handed to the charges inside. Integrating over a volume $V$,

$$\frac{d}{dt}\int_V u\,dV + \oint_{\partial V}\mathbf{S}\cdot d\mathbf{a} = -\int_V \mathbf{J}\cdot\mathbf{E}\,dV.$$

In vacuum $\mathbf{J}=0$, and (8) becomes a pure conservation law: $\partial_t u + \nabla\cdot\mathbf{S} = 0$, a continuity equation for electromagnetic energy with density $u$ and current $\mathbf{S}$.

### 4.2 The plane wave

Take $\mathbf{E} = E_0\cos(kz-\omega t)\,\hat{x}$ and $\mathbf{B} = \frac{E_0}{c}\cos(kz-\omega t)\,\hat{y}$. The energy density splits into two contributions that are **equal point by point**:

$$u_E = \frac{\varepsilon_0}{2}E_0^2\cos^2\varphi = u_B = \frac{1}{2\mu_0}\frac{E_0^2}{c^2}\cos^2\varphi,$$

the equality following from $\varepsilon_0 = 1/(\mu_0 c^2)$. Hence

$$u = \varepsilon_0 E_0^2\cos^2\varphi,$$

and the Poynting vector is

$$\mathbf{S} = \frac{1}{\mu_0}\mathbf{E}\times\mathbf{B} = \frac{E_0^2}{\mu_0 c}\cos^2\varphi\;\hat{z} = c\,u\;\hat{z}.$$

The energy flows along $\hat{\mathbf{k}}$ at the speed of light. Averaging over one period ($\langle\cos^2\varphi\rangle = \tfrac12$):

$$\langle u\rangle = \frac{\varepsilon_0 E_0^2}{2}, \qquad
\langle\mathbf{S}\rangle = \frac{E_0^2}{2\mu_0 c}\,\hat{z} = c\langle u\rangle\,\hat{z}.$$

The magnitude of the time-averaged flux is the **intensity** of the wave,

$$\boxed{I \equiv \langle S\rangle = \frac{E_0^2}{2\mu_0 c} = \frac{c\varepsilon_0 E_0^2}{2}.} \tag{9}$$

Numerically, $I \approx 1.33\times10^{-3}\ \text{W/m}^2$ per $(\text{V/m})^2$ of field amplitude.

The physics in one sentence: the wave's energy is stored half in $\mathbf{E}$ and half in $\mathbf{B}$ in exact synchrony, and it travels as the flux $\mathbf{S} = \mathbf{E}\times\mathbf{B}/\mu_0$ moving at $c$; in vacuum nothing is lost.

---

## 5. Maxwell's equations in matter

### 5.1 Setup: macroscopic fields

Inside material the microscopic fields are averaged into **macroscopic fields** $\mathbf{E}, \mathbf{B}, \mathbf{D}, \mathbf{H}$, with sources split into free ($\rho_f, \mathbf{J}_f$) and bound parts (absorbed into $\mathbf{D}$ and $\mathbf{H}$). The macroscopic equations are

$$\nabla\cdot\mathbf{D} = \rho_f, \qquad \nabla\cdot\mathbf{B} = 0,$$
$$\nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t}, \qquad \nabla\times\mathbf{H} = \mathbf{J}_f + \frac{\partial\mathbf{D}}{\partial t}.$$

The material's response enters through **constitutive relations**. The standard linear, isotropic, homogeneous medium with Ohmic conduction is

$$\mathbf{D} = \varepsilon\,\mathbf{E}, \qquad \mathbf{B} = \mu\,\mathbf{H}, \qquad \mathbf{J}_f = \sigma\,\mathbf{E},$$

where $\varepsilon$ and $\mu$ are the permittivity and permeability of the medium and $\sigma$ its conductivity ($\sigma = 0$: lossless dielectric; $\sigma \to \infty$: perfect conductor). We take the medium source-free, $\rho_f = 0$.

### 5.2 Energy density and Poynting vector in matter

Repeating the derivation of §4.1 with $\mathbf{H}$ and $\mathbf{D}$ in place of $\mathbf{B}/\mu_0$ and $\varepsilon_0\mathbf{E}$, the conduction current now appears as a *sink* of field energy (Joule heating):

$$\boxed{\frac{\partial u}{\partial t} + \nabla\cdot\mathbf{S} = -\mathbf{J}_f\cdot\mathbf{E}, \qquad
u = \frac{1}{2}\left(\mathbf{E}\cdot\mathbf{D} + \mathbf{B}\cdot\mathbf{H}\right), \qquad
\mathbf{S} = \mathbf{E}\times\mathbf{H}.} \tag{10}$$

The full identity $\partial_t u + \nabla\cdot\mathbf{S} + \mathbf{J}_f\cdot\mathbf{E} - (\nabla\times\mathbf{E}+\partial_t\mathbf{B})\cdot\mathbf{H} = 0$ holds for *generic* fields (verified symbolically), so (10) is exact on solutions. For the Ohmic law, $\mathbf{J}_f\cdot\mathbf{E} = \sigma|\mathbf{E}|^2 \ge 0$: field energy is converted to heat at that rate.

Two differences from vacuum: $u = \tfrac12(\varepsilon E^2 + B^2/\mu)$ and $\mathbf{S} = \mathbf{E}\times\mathbf{H} = \mathbf{E}\times\mathbf{B}/\mu$. In a *linear* medium the factor $\tfrac12$ in $u$ is exact; nonlinear or dispersive media require a more careful stored-energy density (Brillouin's formula).

### 5.3 The wave equation in matter

Curl Faraday's law, apply the vector identity, and substitute Ampère's law with the constitutive relations:

$$\nabla\times(\nabla\times\mathbf{E}) = -\frac{\partial}{\partial t}(\nabla\times\mathbf{B}) = -\mu\frac{\partial}{\partial t}(\nabla\times\mathbf{H})
= -\mu\frac{\partial}{\partial t}\left(\sigma\mathbf{E} + \varepsilon\frac{\partial\mathbf{E}}{\partial t}\right).$$

With $\nabla\cdot\mathbf{E} = 0$ (source-free) and constant $\varepsilon, \mu, \sigma$:

$$\boxed{\nabla^2\mathbf{E} = \mu\varepsilon\frac{\partial^2\mathbf{E}}{\partial t^2} + \mu\sigma\frac{\partial\mathbf{E}}{\partial t}.} \tag{11}$$

This is a **damped** wave equation: the extra first-time-derivative term $\mu\sigma\,\partial_t\mathbf{E}$ is the loss. For $\sigma = 0$ it reduces to the vacuum form with propagation speed $v = 1/\sqrt{\mu\varepsilon}$. An identical equation holds for $\mathbf{H}$.

### 5.4 Plane waves and the complex dispersion relation

Insert the plane-wave ansatz $\mathbf{E} = \mathbf{E}_0 e^{i(\mathbf{k}\cdot\mathbf{r}-\omega t)}$ with a **complex** wave vector. Stripping the exponential, the four macroscopic equations give (all verified symbolically):

- $\nabla\cdot\mathbf{D}=0 \Rightarrow \mathbf{k}\cdot\mathbf{E}_0 = 0$ — the wave is still **transverse**;
- $\nabla\times\mathbf{E}=-\partial_t\mathbf{B} \Rightarrow \mathbf{B}_0 = \dfrac{\mathbf{k}\times\mathbf{E}_0}{\omega}$ — unchanged in form;
- $\nabla\cdot\mathbf{B}=0$ — automatic (triple product with repeated vector);
- $\nabla\times\mathbf{H}=\mathbf{J}_f+\partial_t\mathbf{D} \Rightarrow$ the **dispersion relation**

$$\boxed{\mathbf{k}^2 = \mu\varepsilon\omega^2 + i\,\mu\sigma\omega.} \tag{12}$$

Equation (12) is the entire story of propagation in a linear conducting medium. Writing $\mathbf{k} = \kappa\,\hat{\mathbf{k}}$ with $\kappa = \beta + i\alpha$:

$$\beta^2 - \alpha^2 = \mu\varepsilon\omega^2, \qquad 2\alpha\beta = \mu\sigma\omega,$$

where $\beta$ is the **phase** wavenumber (wavelength, phase velocity $v_p = \omega/\beta$) and $\alpha$ is the **attenuation** constant: the field decays as $e^{-\alpha z}$. The **skin depth** is $\delta = 1/\alpha$, and the **intrinsic impedance** of the medium,

$$\eta = \frac{\omega\mu}{\kappa} = \sqrt{\frac{\mu}{\varepsilon - i\sigma/\omega}},$$

is complex when $\sigma \neq 0$, encoding both the amplitude ratio $|\mathbf{H}_0| = |\kappa||\mathbf{E}_0|/\omega$ and a phase lag between $\mathbf{E}$ and $\mathbf{H}$.

**Good-conductor limit.** When conduction current dominates displacement current ($\sigma \gg \omega\varepsilon$):

$$\kappa \approx (1+i)\sqrt{\frac{\mu\sigma\omega}{2}}, \qquad
\delta = \frac{1}{\alpha} = \sqrt{\frac{2}{\mu\sigma\omega}}, \qquad
\eta \approx \sqrt{\frac{\omega\mu}{\sigma}}\,e^{-i\pi/4}.$$

The $\pi/4$ phase means $\mathbf{H}$ lags $\mathbf{E}$ by $45^\circ$ inside a good conductor.

### 5.5 Worked examples (numerically verified)

**Lossless dielectric — "glass" with $n=2$.** Take $\varepsilon = 4\varepsilon_0$, $\mu = \mu_0$. Then $v = c/2$, $n = c\sqrt{\mu\varepsilon} = 2$, and $\eta = \eta_0/2$. For $\mathbf{E} = E_0\cos(kz-\omega t)\hat{x}$, $\mathbf{B} = \tfrac{E_0}{v}\cos(kz-\omega t)\hat{y}$, all four macroscopic Maxwell equations evaluate to exactly zero, and the energy results are

$$u(t) = \varepsilon E_0^2\cos^2\varphi, \qquad \mathbf{S} = \frac{E_0^2}{\mu v}\cos^2\varphi\,\hat{z} = v\,u\,\hat{z},$$
$$\langle u\rangle = \tfrac12\varepsilon E_0^2, \qquad \langle\mathbf{S}\rangle = \frac{E_0^2}{2\eta}\,\hat{z} = \tfrac12\varepsilon v\,E_0^2\,\hat{z}.$$

Compared with vacuum: the speed drops to $c/n$, the impedance to $\eta_0/n$, and the energy flux for a given field amplitude drops by $1/n^2$.

**Lossy conductor — copper at 60 Hz.** With $\sigma = 5.8\times10^7$ S/m, $\mu = \mu_0$, $\varepsilon = \varepsilon_0$, $f = 60$ Hz, solving (12) gives

$$\beta = \alpha \approx 117.2\ \text{m}^{-1}, \qquad \delta = 1/\alpha \approx 8.53\ \text{mm}, \qquad
|\eta| \approx 2.86\times10^{-6}\ \Omega, \quad \angle\eta = -45^\circ.$$

The good-conductor approximation $\delta = \sqrt{2/(\mu\sigma\omega)}$ reproduces the exact value to four significant figures, as expected since the displacement-to-conduction current ratio is $\omega\varepsilon_0/\sigma \approx 5.8\times10^{-17}$. Physically: a field penetrating copper loses a factor $e$ every 8.5 mm, and the surface impedance is only a few micro-ohms — essentially a short circuit, which is why RF currents are confined to a skin only microns thick.

### 5.6 Energy balance: the dispersion relation *is* energy conservation

For the attenuated wave $|\tilde{\mathbf{E}}|^2 e^{-2\alpha z}$, the averaged flux and Joule loss are

$$\langle S_z\rangle = \frac{\beta}{2\omega\mu}|\tilde{E}|^2 e^{-2\alpha z}, \qquad
\langle\mathbf{J}_f\cdot\mathbf{E}\rangle = \frac{\sigma}{2}|\tilde{E}|^2 e^{-2\alpha z}.$$

Symbolic differentiation shows

$$-\frac{d\langle S_z\rangle}{dz} = \langle\mathbf{J}_f\cdot\mathbf{E}\rangle \quad\Longleftrightarrow\quad 2\alpha\beta = \mu\sigma\omega,$$

which is exactly the imaginary part of the dispersion relation (12). The attenuation of the wave is *precisely* accounted for by the Joule heating it deposits — the two statements are the same fact, one from the wave equation, the other from Poynting's theorem. The time-averaged stored energy generalizes to

$$\langle u\rangle = \frac14|\tilde{E}|^2\left(\varepsilon + \frac{\beta^2+\alpha^2}{\omega^2\mu}\right)e^{-2\alpha z}
\;\xrightarrow{\ \sigma\to 0\ }\; \frac12\varepsilon|\tilde{E}|^2 e^{-2\alpha z}.$$

---

## 6. What changes when matter enters

| Quantity | Vacuum | Linear medium |
|---|---|---|
| Constitutive relations | $\mathbf{D}=\varepsilon_0\mathbf{E}$, $\mathbf{B}=\mu_0\mathbf{H}$ | $\mathbf{D}=\varepsilon\mathbf{E}$, $\mathbf{B}=\mu\mathbf{H}$, $\mathbf{J}_f=\sigma\mathbf{E}$ |
| Wave equation | $\nabla^2\mathbf{E} = \mu_0\varepsilon_0\,\ddot{\mathbf{E}}$ | $\nabla^2\mathbf{E} = \mu\varepsilon\,\ddot{\mathbf{E}} + \mu\sigma\,\dot{\mathbf{E}}$ (damped) |
| Dispersion | $k^2 = \mu_0\varepsilon_0\omega^2$ | $k^2 = \mu\varepsilon\omega^2 + i\mu\sigma\omega$ (complex $k$) |
| Speed / index | $c$ | $v = 1/\sqrt{\mu\varepsilon}$, $n = c\sqrt{\mu\varepsilon}$ (lossless) |
| Intrinsic impedance | $\eta_0 \approx 377\ \Omega$ | $\eta = \sqrt{\mu/(\varepsilon - i\sigma/\omega)}$ |
| Energy density | $\tfrac12(\varepsilon_0E^2 + B^2/\mu_0)$ | $\tfrac12(\mathbf{E}\cdot\mathbf{D} + \mathbf{B}\cdot\mathbf{H})$ |
| Poynting vector | $\mathbf{E}\times\mathbf{B}/\mu_0$ | $\mathbf{E}\times\mathbf{H}$ |
| Energy balance | $\partial_t u + \nabla\cdot\mathbf{S} = 0$ | $\partial_t u + \nabla\cdot\mathbf{S} = -\sigma\lvert\mathbf{E}\rvert^2$ |
| Attenuation | none | skin depth $\delta = 1/\alpha$; good conductor $\delta = \sqrt{2/(\mu\sigma\omega)}$ |

The **transverse** structure, the relation $\mathbf{B}_0 = \mathbf{k}\times\mathbf{E}_0/\omega$, and the right-handed $\{\mathbf{E},\mathbf{H},\hat{\mathbf{k}}\}$ triad survive unchanged. Matter only changes the *magnitude* of the field ratio (via $\eta$), the *speed* (via $n$), and adds *attenuation* (via $\alpha$) and a *phase lag* between $\mathbf{E}$ and $\mathbf{H}$ (via complex $\eta$).

### Scope and caveats

This treatment covers **linear, isotropic, homogeneous, nondispersive** media. Real materials are dispersive — $\varepsilon$ and $\sigma$ depend on $\omega$ — which makes $u$ and $\mathbf{S}$ frequency-dependent and calls for the Brillouin energy formula. Anisotropic media (crystals, waveguides) have $\mathbf{D} = \varepsilon_{ij}E_j$, and the waves become elliptically polarized with $\mathbf{E}$ no longer strictly transverse to $\mathbf{k}$. For the standard introductory treatment, however, the picture above is complete.

---

## Appendix: Verification

All algebraic claims in this essay were checked symbolically with SymPy 1.14.0. The scripts:

- `maxwell_plane_wave.py` — plane-wave conditions, dispersion relation, polarization identities, and the explicit $k\hat{z}$ example (all four Maxwell equations evaluate to 0).
- `poynting_derivation.py` — the identity $\mathbf{J}\cdot\mathbf{E} + \partial_t u + \nabla\cdot(\mathbf{E}\times\mathbf{B})/\mu_0 = (\nabla\times\mathbf{E}+\partial_t\mathbf{B})\cdot\mathbf{B}/\mu_0$ for generic fields; plane-wave $u$, $\mathbf{S}$, $\partial_t u + \nabla\cdot\mathbf{S} = 0$, $\mathbf{S} = cu\hat{z}$, and cycle averages.
- `maxwell_matter.py` — Poynting's theorem in matter for generic fields; the lossy dispersion relation $k^2 = \mu\varepsilon\omega^2 + i\mu\sigma\omega$; the damped wave equation; the $n=2$ lossless example (all four macroscopic equations = 0, $\langle\mathbf{S}\rangle = v\langle u\rangle\hat{z} = E_0^2/(2\eta)$); copper at 60 Hz ($\beta$, $\alpha$, $\delta$, $\eta_c$); and the energy-balance identity $-d\langle S_z\rangle/dz = \langle\mathbf{J}_f\cdot\mathbf{E}\rangle \Leftrightarrow 2\alpha\beta = \mu\sigma\omega$.
