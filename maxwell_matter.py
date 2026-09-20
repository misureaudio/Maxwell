"""Maxwell in matter: derivation + verification with sympy.

Medium: linear, isotropic, homogeneous.
    D = eps E,  B = mu H,  J_f = sigma E   (Ohmic conduction)
Macroscopic Maxwell (free sources):
    div D = rho_f,  div B = 0
    curl E = -dB/dt,  curl H = J_f + dD/dt
Source-free: rho_f = 0.

Part 0: Poynting theorem in matter (generic fields, linear constitutive)
Part 1: algebraic conditions for a plane wave (lossy): k.E0 = 0, k^2 = mu*eps*w^2 + i*mu*sigma*w
Part 2: damped wave equation, ansatz substitution
Part 3a: lossless plane wave, n=2 glass (eps=4 eps0, mu=mu0): verify all 4 eqs, S, u, averages
Part 3b: lossy, copper 60 Hz: beta, alpha, skin depth, eta_c, good-conductor limit
Part 3c: energy balance: -d<S>/dz = <Jf.E>  (dispersion relation = energy conservation)
"""
import sympy as sp

x, y, z, t = sp.symbols('x y z t', real=True)
eps, mu, sig = sp.symbols('epsilon mu sigma', positive=True)
eps0, mu0 = sp.symbols('epsilon_0 mu_0', positive=True)
E0x, E0y, E0z = sp.symbols('E0x E0y E0z', real=True)
kx, ky, kz, w = sp.symbols('k_x k_y k_z omega', real=True)

def div(F): return sp.diff(F[0], x) + sp.diff(F[1], y) + sp.diff(F[2], z)
def curl(F): return sp.Matrix([sp.diff(F[2], y) - sp.diff(F[1], z),
                               sp.diff(F[0], z) - sp.diff(F[2], x),
                               sp.diff(F[1], x) - sp.diff(F[0], y)])

# ---------- Part 0: Poynting theorem in matter ----------
Ex = sp.Function('Ex')(x, y, z, t); Ey = sp.Function('Ey')(x, y, z, t); Ez = sp.Function('Ez')(x, y, z, t)
Hx = sp.Function('Hx')(x, y, z, t); Hy = sp.Function('Hy')(x, y, z, t); Hz = sp.Function('Hz')(x, y, z, t)
Ev = sp.Matrix([Ex, Ey, Ez]); Hv = sp.Matrix([Hx, Hy, Hz])
Dv = eps*Ev; Bv = mu*Hv
Jf = curl(Hv) - sp.diff(Dv, t)              # J_f from Ampere
u  = sp.Rational(1, 2)*(Ev.dot(Dv) + Bv.dot(Hv))
S  = Ev.cross(Hv)
faraday = (curl(Ev) + sp.diff(Bv, t)).dot(Hv)
comb = sp.expand(sp.diff(u, t) + div(S) + Jf.dot(Ev) - faraday)
print("Part 0: Poynting theorem in matter (generic fields, D=eps E, B=mu H)")
print("du/dt + div(E x H) + Jf.E - (curl E + dB/dt).H  =", sp.simplify(comb))
print("=> on solutions:  du/dt + div S = -Jf.E,   u = 1/2(E.D + B.H),   S = E x H")
print("   ohmic loss:  Jf.E = sigma |E|^2 >= 0  (Joule heating)")

# ---------- Part 1: plane wave, algebraic conditions (lossy) ----------
f = sp.exp(sp.I*(kx*x + ky*y + kz*z - w*t))
E0 = sp.Matrix([E0x, E0y, E0z]); k = sp.Matrix([kx, ky, kz])
E = E0*f
B0 = k.cross(E0)/w                        # from Faraday: k x E0 = w B0
B = B0*f
H = B/mu; D = eps*E
k2 = kx**2 + ky**2 + kz**2

print("\nPart 1: algebraic conditions (factor exp(i(k.r - wt)) stripped)")
print("div D /f  =", sp.simplify(div(D)/f))
print("div B /f  =", sp.simplify(div(B)/f))
print("Faraday residual (B0 = k x E0/w) /f =", sp.simplify((curl(E) + sp.diff(B, t))/f).T)
amp_res = sp.simplify((curl(H) - sp.diff(D, t) - sig*E)/f)
print("Ampere residual (with B0 = k x E0/w) /f =", amp_res.T)
cand = (sp.I*(k.dot(E0))/(mu*w))*k + (sp.I*(mu*eps*w**2 - k2)/(mu*w) - sig)*E0
print("identity check (residual - candidate) =", sp.simplify(amp_res - cand).T)
print("=> conditions:  (1) k.E0 = 0   (2) k^2 = mu*eps*w^2 + i*mu*sigma*w")

# ---------- Part 2: damped wave equation, ansatz ----------
lapE = sp.Matrix([sum(sp.diff(E[i], v, 2) for v in (x, y, z)) for i in range(3)])
res2 = sp.simplify((lapE - eps*mu*sp.diff(E, t, 2) - mu*sig*sp.diff(E, t))/f)
print("\nPart 2: damped wave equation  lap E = mu eps d2E/dt2 + mu sigma dE/dt")
print("ansatz residual /f  =", sp.simplify(res2).T)
print("lossless (sigma=0)  =", sp.simplify(res2.subs(sig, 0)).T)

# ---------- Part 3a: lossless plane wave, n = 2 glass (PHYSICAL real fields) ----------
c = 1/sp.sqrt(mu0*eps0)
eps_g = 4*eps0; mu_g = mu0
v = 1/sp.sqrt(eps_g*mu_g)
kv, Exv = sp.symbols('k E0x', positive=True)
wv = v*kv
phi = kv*z - wv*t
# physical (real) fields
Eg = sp.Matrix([Exv*sp.cos(phi), 0, 0])
Bg = sp.Matrix([0, (Exv/v)*sp.cos(phi), 0])      # B0 = E0/v
Hg = Bg/mu_g
Dg = eps_g*Eg
print("\nPart 3a: lossless, eps=4 eps0, mu=mu0  (n = 2, v = c/2)")
print("v =", sp.simplify(v), "   B0 = E0/v =", sp.simplify(Exv/v), "   eta = sqrt(mu/eps) =", sp.simplify(sp.sqrt(mu_g/eps_g)))
# verify all four on the real fields
print("verify (all should be 0):")
print("  div D               =", sp.simplify(div(Dg)))
print("  div B               =", sp.simplify(div(Bg)))
print("  (curl E + dB/dt)    =", sp.simplify((curl(Eg) + sp.diff(Bg, t))).T)
print("  (curl H - dD/dt)    =", sp.simplify((curl(Hg) - sp.diff(Dg, t))).T)
ug = sp.Rational(1, 2)*(Eg.dot(Dg) + Bg.dot(Hg))
Sg = Eg.cross(Hg)
T = 2*sp.pi/wv
print("u(t)          =", sp.simplify(ug))
print("S(t)          =", sp.simplify(Sg.T))
uav = sp.integrate(ug, (t, 0, T))/T
Sav = sp.integrate(Sg[2], (t, 0, T))/T
print("<u>           =", sp.simplify(uav))
print("<S_z>         =", sp.simplify(Sav))
print("<S> == v <u> zhat ?", sp.simplify(Sav - v*uav) == 0)
print("<S> == E0^2/(2 eta) ?", sp.simplify(Sav - Exv**2/(2*sp.sqrt(mu_g/eps_g))) == 0)
print("<S> == (1/2) eps v E0^2 ?", sp.simplify(Sav - sp.Rational(1,2)*eps_g*v*Exv**2) == 0)

# ---------- Part 3b: lossy, copper 60 Hz (numeric) ----------
import cmath
mu0n = 4e-7*cmath.pi; eps0n = 8.8541878128e-12
sigc = 5.8e7; wn = 2*cmath.pi*60.0
k2n = eps0n*mu0n*wn**2 + 1j*mu0n*sigc*wn
kn = cmath.sqrt(k2n)                       # branch: Re>0, Im>0
beta, alpha = kn.real, kn.imag
print("\nPart 3b: copper, sigma=5.8e7 S/m, mu=mu0, eps=eps0, f=60 Hz")
print("k^2 = mu eps w^2 + i mu sigma w   (complex)")
print("beta = %.4g   alpha = %.4g   (1/m)" % (beta, alpha))
print("skin depth delta = 1/alpha = %.4g m" % (1/alpha))
print("good-conductor approx: beta=alpha=sqrt(mu sigma w/2) = %.4g,  delta = sqrt(2/(mu sigma w)) = %.4g m"
      % (cmath.sqrt(mu0n*sigc*wn/2).real, cmath.sqrt(2/(mu0n*sigc*wn)).real))
print("check (beta+i alpha)^2 == k^2 :", abs((beta+1j*alpha)**2 - k2n) < 1e-8*abs(k2n))
print("check 2 alpha beta == mu sigma w :", abs(2*alpha*beta - mu0n*sigc*wn) < 1e-12*mu0n*sigc*wn)
etac = wn*mu0n/(beta+1j*alpha)
etac_gc = cmath.sqrt(wn*mu0n/sigc)*cmath.exp(-1j*cmath.pi/4)
print("eta_c = w mu/k = %.4g * exp(i %.4g pi)  |eta_c| = %.4g ohm" % (abs(etac), cmath.phase(etac)/cmath.pi, abs(etac)))
print("good-conductor eta_c = sqrt(w mu/sigma) e^{-i pi/4} = %.4g * exp(i %.4g pi)" % (abs(etac_gc), cmath.phase(etac_gc)/cmath.pi))

# ---------- Part 3c: energy balance for the lossy plane wave ----------
print("\nPart 3c: energy balance  -d<S>/dz = <Jf.E>")
b, a, om, mu_s, sig_s, E0s = sp.symbols('beta alpha omega mu sigma E0', positive=True)
Savg_z = b*E0s**2*sp.exp(-2*a*z)/(2*om*mu_s)          # <S_z> = beta |E~|^2 e^{-2 alpha z}/(2 w mu)
JfE_avg = sig_s*E0s**2*sp.exp(-2*a*z)/2                # <Jf.E> = sigma |E~|^2 e^{-2 alpha z}/2
bal = sp.simplify(-sp.diff(Savg_z, z) - JfE_avg)
print("-d<S>/dz - <Jf.E> =", bal)
print("vanishes  <=>  2 alpha beta = mu sigma omega  (the imaginary part of the dispersion relation)")
# stored energy average
uavg = sp.Rational(1, 4)*E0s**2*(eps + (b**2 + a**2)/(om**2*mu_s))*sp.exp(-2*a*z)
print("<u> = 1/4 |E~|^2 (eps + (beta^2+alpha^2)/(w^2 mu)) e^{-2 alpha z}  (lossless limit -> eps|E~|^2/2 e^{-2alpha z})")
