# The Ansatz in Differential Equations

A companion document: **Part I** is the theory (what an ansatz is and why it is legitimate), **Part II** is a set of fully worked examples, and **Part III** is a one-page cheat sheet.

---

# Part I — Theory

## 1. The word

*Ansatz* is German for "starting point," "assumption," or "what you put forward." In the context of differential equations (DEs) it has a precise technical meaning:

> **An ansatz is a *form* you propose for the unknown solution — a template containing undetermined parameters — before you have actually solved the equation.** You substitute this template back into the DE, and the equation then becomes algebraic (or a simpler equation) that you solve for the unknown parameters.

The crucial point: you are **not** guessing the numerical answer. You are guessing the *shape* of the answer, on the basis of some reason, and letting the equation fill in the details.

## 2. Why a guess is even legitimate

A DE constrains a function, but a DE *family* has infinitely many solutions, so the equation alone rarely pins down a single one. When you add a boundary/initial condition, the solution space shrinks to a finite-dimensional one. The ansatz is your way of *parameterizing* that (hopefully) finite-dimensional space: you write down a function with the right number of free knobs, and the DE tells you what those knobs must be.

Two things make this work in practice:

- **Symmetry.** If the equation and its domain share a symmetry (translation-invariant coefficients, a separable geometry, a periodic forcing), the solution often inherits it, and that symmetry tells you the shape.
- **Structure of the operator.** Linear operators with constant coefficients act on exponentials by multiplying them — exponentials are their eigenfunctions. That single fact drives the most common ansatz of all.

## 3. The general workflow

Every ansatz method follows the same four-step pattern:

1. **Propose a form** $y(x) = \text{template}(x;\, \text{parameters})$.
2. **Substitute** it into the differential equation.
3. **Solve** the resulting (simpler) conditions — usually an algebraic equation — for the parameters.
4. **Verify** the result, and check whether the ansatz is *complete* (i.e. it does not silently miss solutions).

The whole method is only as good as the quality of the reason behind step 1. A good ansatz is *informed*, not random.

## 4. The classic ansätze

### (a) The exponential ansatz — constant-coefficient ODEs

For
$$y'' + ay' + by = 0$$
you propose $y = e^{rx}$. Why? Because $\frac{d^n}{dx^n} e^{rx} = r^n e^{rx}$ — differentiation just multiplies the exponential by $r$, so a linear combination of derivatives *factors out* the $e^{rx}$:

$$e^{rx}(r^2 + ar + b) = 0 \quad\Longrightarrow\quad r^2 + ar + b = 0$$

The DE has collapsed into the **characteristic (auxiliary) polynomial**. The roots $r_1, r_2$ give the solution $y = C_1 e^{r_1 x} + C_2 e^{r_2 x}$ (with the usual modifications for repeated or complex roots). The exponential was the right *shape* because the operator has constant coefficients (translation invariance).

### (b) The monochromatic plane-wave ansatz — PDEs

For the wave equation you propose
$$\psi = \psi_0\, e^{i(\mathbf{k}\cdot\mathbf{x} - \omega t)}$$

The reasoning: the medium is homogeneous (in space) and isotropic, with no time-varying sources, so the equation is invariant under spatial translations and time translations. A function that "respects" those symmetries is a **plane wave** — a single spatial frequency $\mathbf{k}$ and a single temporal frequency $\omega$. Substituting turns $\nabla^2 \to -k^2$ and $\partial_t^2 \to -\omega^2$, and the PDE collapses to the algebraic **dispersion relation** (e.g. $\omega = c\,|\mathbf{k}|$).

This is the single most important ansatz in physics: it converts differential equations into algebra, and the algebraic part is where the real physics (the dispersion relation) lives.

### (c) Separation of variables

For a PDE on a domain with separable geometry (a rectangle, a sphere), you propose the solution *factors*:
$$u(x,t) = X(x)\,T(t)$$
Substitution gives $\frac{T'}{c^2 T} = \frac{X''}{X} = -\lambda$, where the left side depends only on $t$ and the right only on $x$ — they can be equal only if both equal a **separation constant** $\lambda$. One PDE becomes two ODEs. The ansatz is justified by the geometry of the domain; the constants $\lambda$ are then fixed by the boundary conditions (this is where eigenvalues enter).

### (d) Trial solution by undetermined coefficients — inhomogeneous ODEs

For $y'' + y = \cos x$ you *know* the homogeneous part ($e^{\pm i x}$) and need a particular solution. You propose a trial of the *same form as the forcing*, $y_p = A\cos x + B\sin x$, and solve for $A,B$. If the forcing is $e^{kx}$ you try $A e^{kx}$; if it is a polynomial you try a polynomial of the same degree. The rule: **the particular solution has the same functional form as the source term** (for constant-coefficient operators).

### (e) Power series / Frobenius

When you cannot see a closed-form shape, you ansatz the solution as a series:
$$y(x) = \sum_{n=0}^{\infty} a_n (x-x_0)^n$$
Substitution turns the DE into a **recurrence relation** linking $a_{n+1}$ to earlier coefficients. The Frobenius variant, $y = (x-x_0)^r \sum a_n (x-x_0)^n$, handles singular points. The "parameters" are now an infinite sequence, but the recurrence fixes them all from a few initial ones.

### (f) Perturbation ansatz

When the equation contains a small parameter $\varepsilon$ (e.g. a weak nonlinearity), you ansatz the solution as an *expansion in powers of $\varepsilon$*:
$$y = y_0 + \varepsilon y_1 + \varepsilon^2 y_2 + \cdots$$
Substitution and collecting order by order gives a hierarchy of easier problems (solve for $y_0$, then $y_1$, etc.). The ansatz is justified by the existence of a small parameter and a known zeroth-order solution.

### (g) Trial-function (variational) ansätze

For eigenvalue or boundary-value problems you cannot solve exactly, you propose a *finite family* of plausible functions $y(x;\mathbf{a})$ with a few parameters and minimize an energy functional, or project the residual onto a basis (Galerkin / Rayleigh–Ritz). The ansatz is a *basis of trial functions*; the DE is satisfied only approximately, but the error can be made systematically small.

## 5. What an "ansatz" is *not*

- **Not a blind guess.** A pure guess at the numerical answer is not an ansatz. The ansatz is a *structured template*, and the structure must be justified by symmetry, the operator's properties, or a known small parameter.
- **Not always complete.** This is the key caveat. An ansatz can be *too narrow* and miss solutions. Two famous examples:
  - **Resonance in undetermined coefficients.** If the forcing $\cos x$ matches the homogeneous solution, the naive trial $A\cos x + B\sin x$ is already a homogeneous solution and gives no new information — you must *multiply by $x$* (the "resonant" ansatz). A good method includes a rule for when to modify the trial.
  - **Exponential ansatz at repeated/complex roots.** The raw $e^{rx}$ template only gives *distinct* exponentials; repeated roots require the $x e^{rx}$ term. You must check the ansatz spans the full solution space (dimension = order of the DE).
- **Not a proof of existence.** Finding *one* solution via an ansatz does not by itself prove you have found *all* of them. Completeness is a separate check.

## 6. The discipline of using an ansatz well

A rigorous ansatz method always closes with a check. The checklist:

1. **Justification** — why this shape? (symmetry, operator structure, small parameter, domain geometry.)
2. **Sufficiency of parameters** — does the template have as many free parameters as the DE's order / boundary conditions require? If not, it is under-parameterized and will miss solutions.
3. **Substitution & solve** — the DE must be satisfied identically; solve the resulting conditions.
4. **Completeness** — confirm the resulting family has the expected dimension; if the operator is linear, confirm you can superpose; check the special cases (resonance, repeated roots, singular points) where the basic template fails.
5. **Boundary/initial conditions** — the ansatz usually leaves free constants; these are what the conditions fix.

---

# Part II — Worked examples

Each example follows the four-step workflow (propose → substitute → solve → verify) and closes with the completeness check.

## Example 1 — Exponential ansatz on a homogeneous ODE (complex roots)

**Problem.** Solve
$$y'' + 4y' + 5y = 0.$$

**Step 1 — Propose.** Constant coefficients → translation invariance → exponential ansatz
$$y = e^{rx}.$$

**Step 2 — Substitute.** Since $y' = r e^{rx}$ and $y'' = r^2 e^{rx}$,
$$e^{rx}\big(r^2 + 4r + 5\big) = 0 \quad\Longrightarrow\quad r^2 + 4r + 5 = 0.$$

**Step 3 — Solve.**
$$r = \frac{-4 \pm \sqrt{4^2 - 4\cdot 5}}{2} = \frac{-4 \pm \sqrt{-4}}{2} = -2 \pm i.$$
Complex conjugate roots $r = \alpha \pm i\beta$ with $\alpha = -2$, $\beta = 1$ give the two independent *real* solutions $e^{\alpha x}\cos(\beta x)$ and $e^{\alpha x}\sin(\beta x)$:
$$\boxed{\,y(x) = e^{-2x}\big(C_1\cos x + C_2\sin x\big).\,}$$

**Step 4 — Verify & completeness.** Differentiate:
$y' = e^{-2x}\big[-2(C_1\cos x + C_2\sin x) + (-C_1\sin x + C_2\cos x)\big]$, and a direct substitution (or the standard theorem) confirms the DE. The two constants $C_1, C_2$ match the order of the DE, so the family is complete. Physically: a **damped oscillation** — the real part $\alpha=-2$ gives the exponential decay, the imaginary part $\beta=1$ the oscillation.

---

## Example 2 — Undetermined coefficients and the resonance pitfall

**Problem.** Solve
$$y'' + y = \cos x.$$

**Step 1 — Homogeneous part.** $r^2 + 1 = 0 \Rightarrow r = \pm i$, so
$$y_h = C_1\cos x + C_2\sin x.$$

**Step 2 — Propose a particular solution.** The forcing is $\cos x$, so the naive trial is
$$y_p = A\cos x + B\sin x.$$
**But** this has the *same form* as $y_h$ — it is already a homogeneous solution, so substituting it gives $0 = \cos x$, a contradiction. This is **resonance**: the forcing frequency coincides with a natural frequency of the homogeneous operator.

**Resonant ansatz.** Multiply the trial by $x$:
$$y_p = x\big(A\cos x + B\sin x\big) = Ax\cos x + Bx\sin x.$$

**Step 3 — Substitute.** Compute the derivatives:
$$y_p' = (A + Bx)\cos x + (B - Ax)\sin x$$
$$y_p'' = (2B - Ax)\cos x + (-2A - Bx)\sin x$$
Then
$$y_p'' + y_p = \big(2B - Ax + Ax\big)\cos x + \big(-2A - Bx + Bx\big)\sin x = 2B\cos x - 2A\sin x.$$
Set equal to the forcing $\cos x$ and match coefficients:
$$2B = 1 \Rightarrow B = \tfrac{1}{2}, \qquad -2A = 0 \Rightarrow A = 0.$$

**Step 4 — Verify & completeness.**
$$y_p = \tfrac{x}{2}\sin x,\qquad y_p' = \tfrac{1}{2}\sin x + \tfrac{x}{2}\cos x,\qquad y_p'' = \cos x - \tfrac{x}{2}\sin x,$$
so $y_p'' + y_p = \cos x$. ✓ General solution:
$$\boxed{\,y(x) = C_1\cos x + C_2\sin x + \tfrac{x}{2}\sin x.\,}$$
The extra $\tfrac{x}{2}\sin x$ term grows without bound — the hallmark of resonance (energy pumped in phase with the natural mode).

**Lesson.** The naive ansatz *failed* and a completeness/justification check caught it. Always ask: *is my trial already in the homogeneous solution space?*

---

## Example 3 — Plane-wave ansatz on the wave equation (PDE)

**Problem.** Solve the scalar wave equation in a homogeneous medium
$$\nabla^2 \psi - \frac{1}{c^2}\frac{\partial^2 \psi}{\partial t^2} = 0.$$

**Step 1 — Propose.** The equation is invariant under spatial and time translations → plane-wave ansatz
$$\psi(\mathbf{x},t) = \psi_0\, e^{i(\mathbf{k}\cdot\mathbf{x} - \omega t)}.$$

**Step 2 — Substitute.** The derivatives act as:
$$\nabla^2 \psi = -|\mathbf{k}|^2\,\psi = -k^2\psi, \qquad \frac{\partial^2 \psi}{\partial t^2} = -\omega^2\,\psi.$$
So
$$\big(-k^2\big)\psi - \frac{1}{c^2}\big(-\omega^2\big)\psi = \left(k^2 - \frac{\omega^2}{c^2}\right)\psi = 0.$$

**Step 3 — Solve.** For a nontrivial $\psi_0 \neq 0$:
$$k^2 = \frac{\omega^2}{c^2} \quad\Longrightarrow\quad \boxed{\,\omega = c\,|\mathbf{k}|\,}$$
(the **dispersion relation**). The PDE has collapsed to one algebraic equation.

**Step 4 — Verify & completeness.** Substitution is exact, so every monochromatic plane wave with $\omega = ck$ is a solution. Because the equation is *linear with constant coefficients*, the full general solution is a **superposition** (Fourier integral) of such plane waves:
$$\psi(\mathbf{x},t) = \int \tilde\psi_0(\mathbf{k})\, e^{i(\mathbf{k}\cdot\mathbf{x} - \omega(\mathbf{k}) t)}\, d^3k, \qquad \omega(\mathbf{k}) = c|\mathbf{k}|.$$
So the single-mode ansatz is a *basis* for the whole solution space — complete in the sense of a Fourier basis.

**Connection to Maxwell.** This is precisely the ansatz used in the wave-equation derivations: $\mathbf{E} = \mathbf{E}_0 e^{i(\mathbf{k}\cdot\mathbf{x}-\omega t)}$ gives $\omega = c|\mathbf{k}|$, and the *remaining* Maxwell equations (Faraday, Gauss) then fix the free amplitude and polarization: $\mathbf{B}_0 = \hat{\mathbf{k}}\times\mathbf{E}_0/c$ (transversality, $\mathbf{k}\cdot\mathbf{E}_0 = 0$). The ansatz collapses the differential part to algebra; the other equations fix what the ansatz left open.

---

## Example 4 — Side by side: the ODE characteristic polynomial is a PDE dispersion relation

Examples 1 and 3 look different but are the *same operation*. Both operators have constant coefficients, so the exponential ansatz turns every derivative into a multiplication by a "frequency." The only difference is how many frequencies are present.

**Left — the ODE** $y'' + 4y' + 5y = 0$, ansatz $y = e^{rt}$ (one frequency $r$):

| derivative | result |
|---|---|
| $y$ | $e^{rt}$ |
| $y'$ | $r\,e^{rt}$ |
| $y''$ | $r^2 e^{rt}$ |

Factoring out $e^{rt}$:
$$r^2 + 4r + 5 = 0 \quad\text{(characteristic polynomial in one frequency } r\text{).}$$

**Right — the 1D wave equation** $\frac{1}{c^2}u_{tt} - u_{xx} = 0$, ansatz $u = e^{i(kx - \omega t)}$ (two frequencies $k, \omega$):

| derivative | result |
|---|---|
| $u$ | $e^{i(kx-\omega t)}$ |
| $u_t$ | $-i\omega\, u$ |
| $u_{tt}$ | $-\omega^2 u$ |
| $u_x$ | $ik\, u$ |
| $u_{xx}$ | $-k^2 u$ |

Factoring out the exponential:
$$-\frac{\omega^2}{c^2} + k^2 = 0 \quad\Longrightarrow\quad \omega^2 = c^2 k^2 \quad\text{(dispersion relation in two frequencies } k,\omega\text{).}$$

**The unifying statement.** Substituting the exponential ansatz always yields an algebraic equation in the frequencies — a **dispersion relation**. The ODE characteristic polynomial is simply the special case with a single frequency.

To see it directly, rewrite the ODE with the physics-style convention $y = e^{-i\omega t}$ (so $y' \to -i\omega$, $y'' \to -\omega^2$):
$$(-\omega^2) + 4(-i\omega) + 5 = 0 \quad\Longrightarrow\quad \omega^2 + 4i\omega - 5 = 0.$$
This is a dispersion relation in $\omega$ — the same object as the ODE's characteristic equation, just written in frequency language. Its roots are $\omega = -2 \pm i$ (the same $r$ from Example 1 with $r = -i\omega$), giving the damped-oscillation behaviour.

> **Take-away.** "Characteristic polynomial" and "dispersion relation" are one idea: the algebraic condition you get when a constant-coefficient operator acts on an exponential. An ODE has one frequency; a PDE has as many as it has independent variables.

---

# Part III — Cheat sheet

| Ansatz | Used for | Why it works | What substitution gives |
|---|---|---|---|
| $e^{rx}$ | constant-coeff. homogeneous ODE | translation invariance | characteristic polynomial in $r$ |
| $e^{i(\mathbf{k}\cdot\mathbf{x}-\omega t)}$ | wave / PDE in homogeneous medium | space+time translation invariance | dispersion relation $\omega(\mathbf{k})$ |
| $X(x)\,T(t)$ | PDE on separable geometry | domain geometry | two ODEs + separation constant |
| same form as forcing | constant-coeff. inhom. ODE | operator maps the forcing form to itself | algebraic system for coefficients |
| $\sum a_n (x-x_0)^n$ | unknown closed form / singular points | analyticity | recurrence for $a_n$ |
| $\sum_{n\ge0}\varepsilon^n y_n$ | small parameter $\varepsilon$ | regular perturbation | hierarchy of easier DEs |
| finite trial basis | eigenvalue / BVP, inexact | variational / projection | algebraic eigenvalue problem |

**The four-step workflow (always):**
1. **Propose** a form with undetermined parameters.
2. **Substitute** into the DE.
3. **Solve** the resulting algebraic / simpler conditions.
4. **Verify** and check **completeness** (dimension, resonance, repeated roots, singular points).

**The one rule that prevents most mistakes:** before substituting, ask *"is my trial function already in the homogeneous solution space?"* If yes, you are at resonance and must modify the trial (typically multiply by $x$ or raise the polynomial degree).

**The unifying idea:** for constant-coefficient operators, the exponential ansatz converts the DE into an algebraic **dispersion relation** in the frequencies — an ODE characteristic polynomial is that relation with a single frequency.
