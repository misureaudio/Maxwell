"""Plane-wave solution of vacuum Maxwell equations, derived symbolically with sympy.

Vacuum Maxwell:
    div E = 0,  div B = 0
    curl E = -dB/dt,  curl B = mu0*eps0 * dE/dt

Ansatz: E(x,t) = E0 * exp(i(k.r - wt)), B = B0 * exp(i(k.r - wt))
"""
import sympy as sp

# --- symbols ---
x, y, z, t = sp.symbols('x y z t', real=True)
kx, ky, kz = sp.symbols('k_x k_y k_z', real=True)
w = sp.symbols('omega', positive=True)
Ex0, Ey0, Ez0 = sp.symbols('E0x E0y E0z', real=True)
Bx0, By0, Bz0 = sp.symbols('B0x B0y B0z', real=True)
eps0, mu0 = sp.symbols('epsilon_0 mu_0', positive=True)

theta = kx*x + ky*y + kz*z - w*t
f = sp.exp(sp.I*theta)
E = sp.Matrix([Ex0, Ey0, Ez0])*f
B = sp.Matrix([Bx0, By0, Bz0])*f
k  = sp.Matrix([kx, ky, kz])
E0 = sp.Matrix([Ex0, Ey0, Ez0])
B0 = sp.Matrix([Bx0, By0, Bz0])

def div(F):
    return sp.diff(F[0], x) + sp.diff(F[1], y) + sp.diff(F[2], z)

def curl(F):
    return sp.Matrix([sp.diff(F[2], y) - sp.diff(F[1], z),
                      sp.diff(F[0], z) - sp.diff(F[2], x),
                      sp.diff(F[1], x) - sp.diff(F[0], y)])

print("=== Maxwell with plane-wave ansatz, common factor exp(i(k.r - wt)) stripped ===")
print("div E /f        =", sp.simplify(div(E)/f))
print("div B /f        =", sp.simplify(div(B)/f))
print("curl E /f       =", sp.simplify(curl(E)/f).T)
print("curl B /f       =", sp.simplify(curl(B)/f).T)
print("dE/dt /f        =", sp.simplify(sp.diff(E, t)/f).T)
print("dB/dt /f        =", sp.simplify(sp.diff(B, t)/f).T)

c1 = k.dot(E0)      # k . E0
c2 = k.dot(B0)      # k . B0
far = k.cross(E0) - w*B0           # Faraday  -> k x E0 = w B0
amp = k.cross(B0) + mu0*eps0*w*E0  # Ampere   -> k x B0 = -mu0 eps0 w E0
print("\nFaraday residual  k x E0 - w B0         =", far.T)
print("Ampere  residual  k x B0 + mu0 eps0 w E0 =", amp.T)

# --- substitute B0 = (k x E0)/w into Ampere residual ---
res = sp.expand(amp.subs(B0, k.cross(E0)/w))
print("\nAmpere residual with B0 = (k x E0)/w:", res.T)
k2 = kx**2 + ky**2 + kz**2
factored = sp.expand((c1/w)*k + (mu0*eps0*w - k2/w)*E0)
print("identity check (diff of the two forms):", sp.simplify(res - factored).T)
print("\n=> two conditions remain:")
print("   (1) k.E0 = 0")
print("   (2) mu0*eps0*w - k^2/w = 0   =>   k^2 =", sp.simplify(mu0*eps0*w**2))

# --- consequences ---
B0sol = k.cross(E0)/w
print("\nE0 . B0  =", sp.simplify(E0.dot(B0sol)), "  (triple product, two equal vectors)")
print("with k.E0=0: |k x E0|^2 = k^2|E0|^2 - (k.E0)^2 =", sp.simplify(k2*(E0.dot(E0)) - c1**2))

# --- concrete example: k = k zhat, E0 = Ex xhat, w = c k ---
cval = 1/sp.sqrt(mu0*eps0)
kv   = sp.symbols('k', positive=True)
Exv  = sp.symbols('Ex', positive=True)
E0v  = sp.Matrix([Exv, 0, 0])
B0v  = sp.simplify((sp.Matrix([0, 0, kv]).cross(E0v))/(cval*kv))
print("\nExample: k=(0,0,k), E0=(Ex,0,0), w=c k  =>  B0 =", B0v.T)
sub = {kx:0, ky:0, kz:kv, w:cval*kv, Ex0:E0v[0], Ey0:0, Ez0:0,
       Bx0:B0v[0], By0:B0v[1], Bz0:B0v[2]}
print("\nVerify all four equations (each should be 0):")
print("  div E /f                  =", sp.simplify(div(E).subs(sub)/f))
print("  div B /f                  =", sp.simplify(div(B).subs(sub)/f))
print("  (curl E + dB/dt)/f        =", sp.simplify((curl(E) + sp.diff(B, t)).subs(sub)/f).T)
print("  (curl B - mu0 eps0 dE/dt) =", sp.simplify((curl(B) - mu0*eps0*sp.diff(E, t)).subs(sub)/f).T)
print("\nE x B /f (Poynting direction) =", sp.simplify(E.cross(B).subs(sub)/f).T)
