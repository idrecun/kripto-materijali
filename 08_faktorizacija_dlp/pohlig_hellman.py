import itertools
from sympy.ntheory.modular import crt

# We assume n is B-powersmooth so this is fine
def factorize(n):
    factors = {}
    B = 2
    while B <= n:
        if n % B == 0:
            factors[B] = 0
        while n % B == 0:
            n //= B
            factors[B] += 1
        B += 1
    return factors

def dlp_bruteforce(g, h, p):
    t = 1
    for i in itertools.count():
        if t == h:
            return i
        t = (g * t) % p

# The real Pohlig-Hellman doesn't brute-force DLP for pi^ni in O(pi^ni), but instead does it in O(ni sqrt(pi))
# This is still fine since we assume that p-1 is B-powersmooth, meaning O(pi^ni) = O(B)
def dlp(g, h, p):
    n = p - 1
    base = factorize(n)
    xs = []
    ps = []
    for pi, ni in base.items():
        pt = pow(pi, ni)
        gi = pow(g, n // pt, p)
        hi = pow(h, n // pt, p)
        xi = dlp_bruteforce(gi, hi, p)
        xs.append(xi)
        ps.append(pt)
    x, _ = crt(ps, xs)
    return x
