import secrets
import diffie_hellman as dh
from math import gcd
from sympy import mod_inverse

def encode(message):
    return int(message.encode('utf-8').hex(), 16)

def decode(message):
    return bytes.fromhex(hex(message)[2:]).decode('utf-8')

def generate_keys():
    while True:
        enc_key = secrets.randbelow(dh.p - 2) + 1
        if gcd(enc_key, dh.p - 1) == 1:
            dec_key = mod_inverse(enc_key, dh.p - 1)
            return enc_key, dec_key

def encrypt(e, m):
    return pow(m, e, dh.p)

def decrypt(d, m):
    return pow(m, d, dh.p)
