from math import gcd, isqrt

def pollard(n, B):
    a = 2
    for b in range(2, B):
        a = pow(a, b, n)
        g = gcd(a-1, n)
        if 1 < g < n:
            return g

def factorize(n):
    return pollard(n, isqrt(n) + 1)
