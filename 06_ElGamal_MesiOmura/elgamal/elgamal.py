import diffie_hellman as dh
from sympy import mod_inverse

def encode(message):
    return int(message.encode('utf-8').hex(), 16)

def decode(message):
    return bytes.fromhex(hex(message)[2:]).decode('utf-8')

def encrypt(priv_key, oth_pub_key, message):
    S = dh.shared_key(priv_key, oth_pub_key)
    return (message * S) % dh.p

def decrypt(priv_key, oth_pub_key, ciphertext):
    S = dh.shared_key(priv_key, oth_pub_key)
    return (ciphertext * mod_inverse(S, dh.p)) % dh.p
