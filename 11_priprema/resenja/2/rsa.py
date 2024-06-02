from Crypto.Util import number
import secrets
from math import gcd

def generateKeyPair():
    p = number.getPrime(1024)
    q = number.getPrime(1024)
    phi = (p - 1) * (q - 1)
    n = p * q

    while True:
        enc_key = secrets.randbelow(phi) + 1
        if gcd(enc_key, phi) == 1:
            dec_key = pow(enc_key, -1, phi)
            return dec_key, (n, enc_key)

def encrypt(n, enc_key, message):
    return pow(message, enc_key, n)

def decrypt(n, dec_key, ciphertext):
    return pow(ciphertext, dec_key, n)

def sign(priv, pub, message):
    return pow(message, priv, pub[0])

def verify(pub, signature, message):
    return message == pow(signature, pub[1], pub[0])
