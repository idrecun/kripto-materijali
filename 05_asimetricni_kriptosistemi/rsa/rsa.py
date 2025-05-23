from Crypto.Util import number
import secrets
from math import gcd

def generate():
    p = number.getPrime(1024)
    q = number.getPrime(1024)
    phi = (p - 1) * (q - 1)
    n = p * q

    while True:
        enc_key = secrets.randbelow(phi) + 1
        if gcd(enc_key, phi) == 1:
            dec_key = pow(enc_key, -1, phi)
            return n, enc_key, dec_key

def encrypt(n, enc_key, message):
    return pow(message, enc_key, n)

def decrypt(n, dec_key, ciphertext):
    return pow(ciphertext, dec_key, n)

def sign(n, dec_key, message):
    return message, pow(message, dec_key, n)

def verify(n, enc_key, message, signature):
    return message == pow(signature, enc_key, n)
