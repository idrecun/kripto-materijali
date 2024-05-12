# b=g^a (mod p)
# b=g^xk+y
# bg^-xk=g^y
from sympy import mod_inverse
from math import isqrt

def log(g, b, p):
    k = isqrt(p) + 1

    ys = {}
    for y in range(k):
        ys[pow(g, y, p)] = y

    gk = pow(g, k, p)
    gki = mod_inverse(gk, p)
    for x in range(k):
        if b in ys:
            return x * k + ys[b]
        b = (b * gki) % p

    return None
