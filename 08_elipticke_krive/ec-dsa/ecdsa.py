import secrets
import ec
from hashlib import sha256

def generate():
    d = secrets.randbelow(ec.secp256k1.n - 2) + 1
    Q = d * ec.G
    return d, Q

def sign(private_key, message):
    h = int.from_bytes(sha256(message.encode()).digest(), 'big')
    
    while True:
        k = secrets.randbelow(ec.secp256k1.n - 2) + 1
        R = k * ec.G
        r = R.x % ec.secp256k1.n
        if r == 0:
            continue
            
        s = (pow(k, -1, ec.secp256k1.n) * (h + r * private_key)) % ec.secp256k1.n
        if s == 0:
            continue
            
        return r, s

def verify(public_key, message, signature):
    r, s = signature
    
    if not (0 < r < ec.secp256k1.n and 0 < s < ec.secp256k1.n):
        return False
    
    h = int.from_bytes(sha256(message.encode()).digest(), 'big')
    w = pow(s, -1, ec.secp256k1.n)
    u1 = (h * w) % ec.secp256k1.n
    u2 = (r * w) % ec.secp256k1.n
    R = u1 * ec.G + u2 * public_key
    
    return R.x % ec.secp256k1.n == r 