"""
Digital Signature Algorithm (DSA).
"""

from hashlib import sha256
from random import randrange
from Crypto.Util import number

def generate_params():
    """
    Generate DSA parameters (p, q, g).
    For demonstration, we use smaller parameters than in practice.
    """
    q = number.getPrime(160)  # 160-bit prime
    # Find p = kq + 1 that is prime
    while True:
        k = number.getRandomNBitInteger(863)  # (1024-161) bits
        p = k * q + 1
        if number.isPrime(p):
            break
    
    # Find generator g
    while True:
        h = number.getRandomRange(2, p-1)
        g = pow(h, k, p)
        if g != 1:
            break
    
    return p, q, g

def generate_keypair(p=None, q=None, g=None):
    """
    Generisanje para ključeva.
    Privatni ključ: x
    Javni ključ: (p, q, g, y = g^x)
    """
    if p is None or q is None or g is None:
        p, q, g = generate_params()
        
    x = randrange(2, q)  # privatni ključ
    y = pow(g, x, p)     # javni ključ
    return x, (p, q, g, y)

def sign(private_key, public_key, message):
    """
    Potpisivanje poruke.
    """
    x = private_key
    p, q, g, _ = public_key

    # Heširamo poruku
    h = int.from_bytes(sha256(message.encode()).digest(), 'big')

    while True:
        # Biramo slučajan broj k
        k = randrange(2, q)
        
        # Računamo r = (g^k mod p) mod q
        r = pow(g, k, p) % q
        if r == 0:
            continue

        # Računamo s = k^(-1)(h + xr) mod q
        k_inv = pow(k, -1, q)
        s = (k_inv * (h + x * r)) % q
        if s == 0:
            continue

        return r, s

def verify(public_key, message, signature):
    """
    Verifikacija potpisa.
    """
    p, q, g, y = public_key
    r, s = signature

    # Proveravamo da li je potpis u opsegu
    if not (0 < r < q and 0 < s < q):
        return False

    # Heširamo poruku
    h = int.from_bytes(sha256(message.encode()).digest(), 'big')

    # Računamo w = s^(-1) mod q
    w = pow(s, -1, q)

    # Računamo u1 = hw mod q
    u1 = (h * w) % q

    # Računamo u2 = rw mod q
    u2 = (r * w) % q

    # Računamo v = (g^u1 * y^u2 mod p) mod q
    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q

    return v == r 