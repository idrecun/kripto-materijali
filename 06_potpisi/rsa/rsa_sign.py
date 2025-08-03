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
        verify_key = secrets.randbelow(phi) + 1
        if gcd(verify_key, phi) == 1:
            sign_key = pow(verify_key, -1, phi)
            return n, verify_key, sign_key

def sign(n, sign_key, message):
    h = int.from_bytes(sha256(message.encode()).digest(), 'big') % n
    return pow(h, sign_key, n)

def verify(n, verify_key, message, signature):
    h = int.from_bytes(sha256(message.encode()).digest(), 'big') % n
    h_verify = pow(signature, verify_key, n)
    return h == h_verify 