import itertools
from sympy.ntheory.modular import crt

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

def pohlig_hellman(g, h, p):
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
