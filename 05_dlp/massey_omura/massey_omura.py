import secrets
import diffie_hellman as dh
from math import gcd

# Encodes a string into an integer
def encode(message):
    return int(message.encode('utf-8').hex(), 16)

# Decodes a string from an integer
def decode(message):
    return bytes.fromhex(hex(message)[2:]).decode('utf-8')

def generate_keys():
    while True:
        enc_key = secrets.randbelow(dh.p - 2) + 1
        if gcd(enc_key, dh.p - 1) == 1:
            dec_key = pow(enc_key, -1, dh.p - 1)
            return enc_key, dec_key

def encrypt(e, m):
    return pow(m, e, dh.p)

def decrypt(d, m):
    return pow(m, d, dh.p)
