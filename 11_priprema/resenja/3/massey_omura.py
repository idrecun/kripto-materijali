import secrets
import ec
from math import gcd

def generateKeyPair():
    while True:
        enc_key = secrets.randbelow(ec.n - 2) + 1
        if gcd(enc_key, ec.n) == 1:
            dec_key = pow(enc_key, -1, ec.n)
            return enc_key, dec_key

def encrypt(e, M):
    return e * M

def decrypt(d, M):
    return d * M
