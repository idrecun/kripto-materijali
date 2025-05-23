"""
Schnorr digitalni potpisi.
"""

from hashlib import sha256
from random import randrange
from Crypto.Util import number

def generate_params():
    """
    Generate Schnorr parameters (p, q, g).
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

def hash_message(message, r):
    """
    Heš funkcija koja kombinuje poruku i vrednost r.
    """
    h = sha256()
    h.update(str(r).encode())
    h.update(message.encode())
    return int.from_bytes(h.digest(), 'big')

def sign(private_key, public_key, message):
    """
    Potpisivanje poruke.
    """
    x = private_key
    p, q, g, _ = public_key

    # Biramo slučajan broj k
    k = randrange(2, q)

    # Računamo r = g^k mod p
    r = pow(g, k, p)

    # Računamo e = H(r || m)
    e = hash_message(message, r)

    # Računamo s = k + xe mod q
    s = (k + x * e) % q

    return r, s

def verify(public_key, message, signature):
    """
    Verifikacija potpisa.
    """
    p, q, g, y = public_key
    r, s = signature

    # Računamo e = H(r || m)
    e = hash_message(message, r)

    # Proveravamo da li je g^s = r * y^e mod p
    left = pow(g, s, p)
    right = (r * pow(y, e, p)) % p

    return left == right 