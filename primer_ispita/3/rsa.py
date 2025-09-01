import secrets
from math import gcd


def generate():
    p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
    q = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
    # TODO: Implement me
    n = p * q
    phi = (p - 1) * (q - 1)
    while True:
        e = secrets.randbelow(phi - 2) + 2
        if gcd(e, phi) == 1:
            d = pow(e, -1, phi)
            return n, e, d


def encrypt(n, e, m: int):
    # TODO: Implement me
    return pow(m, e, n)


def decrypt(n, d, c: int):
    # TODO: Implement me
    return pow(c, d, n)


