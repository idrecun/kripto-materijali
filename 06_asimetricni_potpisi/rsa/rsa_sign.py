"""
RSA digitalni potpisi.
"""

from hashlib import sha256
from random import randrange
from math import gcd
from Crypto.Util import number

def generate_params():
    """
    Generisanje RSA parametara (p, q).
    """
    p = number.getPrime(1024)
    q = number.getPrime(1024)
    return p, q

def generate_keypair(p=None, q=None):
    """
    Generisanje para ključeva.
    Privatni ključ: (p, q, d)
    Javni ključ: (N, e)
    """
    if p is None or q is None:
        p, q = generate_params()
        
    N = p * q
    phi = (p - 1) * (q - 1)

    # Biramo e tako da je gcd(e, phi) = 1
    e = 65537  # Ferma broj, često se koristi u praksi
    while gcd(e, phi) != 1:
        e = randrange(3, phi, 2)

    # Računamo d = e^(-1) mod phi
    d = pow(e, -1, phi)

    return (p, q, d), (N, e)

def sign(private_key, message):
    """
    Potpisivanje poruke.
    """
    p, q, d = private_key
    N = p * q

    # Heširamo poruku
    h = int.from_bytes(sha256(message.encode()).digest(), 'big')
    h = h % N  # Osiguravamo da je heš manji od N

    # Potpisujemo heš
    s = pow(h, d, N)
    return s

def verify(public_key, message, signature):
    """
    Verifikacija potpisa.
    """
    N, e = public_key

    # Računamo heš poruke
    h = int.from_bytes(sha256(message.encode()).digest(), 'big')
    h = h % N

    # Verifikujemo potpis
    h_verify = pow(signature, e, N)
    return h == h_verify 