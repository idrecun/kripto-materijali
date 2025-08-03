"""
RSA digitalni potpisi.
"""

from Crypto.Util import number
import secrets
from math import gcd
from hashlib import sha256

def generate():
    p = number.getPrime(1024)
    q = number.getPrime(1024)
    phi = (p - 1) * (q - 1)
    n = p * q

    while True:
        sign_key = secrets.randbelow(phi) + 1
        if gcd(sign_key, phi) == 1:
            verify_key = pow(sign_key, -1, phi)
            return n, verify_key, sign_key

def sign(n, sign_key, message):
    # Heširamo poruku
    h = int.from_bytes(sha256(message.encode()).digest(), 'big')
    h = h % n  # Osiguravamo da je heš manji od n
    return pow(h, sign_key, n)

def verify(n, verify_key, message, signature):
    # Računamo heš poruke
    h = int.from_bytes(sha256(message.encode()).digest(), 'big')
    h = h % n
    # Verifikujemo potpis
    h_verify = pow(signature, verify_key, n)
    return h == h_verify 