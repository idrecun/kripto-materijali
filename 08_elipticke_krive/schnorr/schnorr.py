import secrets
import ec
from hashlib import sha256

def generate():
    d = secrets.randbelow(ec.secp256k1.n - 2) + 1
    Q = d * ec.G
    return d, Q

def hash_point_message(R, Q, message):
    h = sha256()
    h.update(str(R.x).encode())
    h.update(str(R.y).encode())
    h.update(str(Q.x).encode())
    h.update(str(Q.y).encode())
    h.update(message.encode())
    return int.from_bytes(h.digest(), 'big')

def sign(private_key, message):
    d = private_key
    Q = d * ec.G
    
    k = secrets.randbelow(ec.secp256k1.n - 2) + 1
    R = k * ec.G
    e = hash_point_message(R, Q, message)
    s = (k + e * d) % ec.secp256k1.n
    
    return R, s

def verify(public_key, message, signature):
    R, s = signature
    Q = public_key
    
    e = hash_point_message(R, Q, message)
    left = s * ec.G
    right = R + e * Q
    
    return left == right 