import secrets
from math import gcd
import ec

def encode(message):
    return ec.secp256k1.encode_message(int(message.encode('utf-8').hex(), 16))

def decode(message):
    return bytes.fromhex(hex(ec.secp256k1.decode_message(message))[2:]).decode('utf-8')

def generate_keys():
    while True:
        enc_key = secrets.randbelow(ec.n - 2) + 1
        if gcd(enc_key, ec.n) == 1:
            dec_key = pow(enc_key, -1, ec.n)
            return enc_key, dec_key

def encrypt(e, M):
    return e * M

def decrypt(d, M):
    return d * M
