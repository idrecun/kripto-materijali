import secrets
import ec
from hashlib import sha256

def private_key():
    """
    Generate a random private key.
    """
    return secrets.randbelow(ec.secp256k1.n - 2) + 1

def public_key(d):
    """
    Calculate the public key Q = dG.
    """
    return d * ec.G

def hash_point_message(R, Q, message):
    """
    Hash function that combines a point R, public key Q, and message.
    """
    h = sha256()
    h.update(str(R.x).encode())
    h.update(str(R.y).encode())
    h.update(str(Q.x).encode())
    h.update(str(Q.y).encode())
    h.update(message.encode())
    return int.from_bytes(h.digest(), 'big')

def sign(private_key, message):
    """
    Sign a message using Schnorr signature scheme.
    Returns (R, s) where R is a curve point and s is an integer.
    """
    d = private_key
    Q = public_key(d)
    
    # Generate random k
    k = secrets.randbelow(ec.secp256k1.n - 2) + 1
    
    # Calculate R = kG
    R = k * ec.G
    
    # Calculate e = H(R || Q || m)
    e = hash_point_message(R, Q, message)
    
    # Calculate s = k + e*d mod n
    s = (k + e * d) % ec.secp256k1.n
    
    return R, s

def verify(public_key, message, signature):
    """
    Verify a Schnorr signature.
    """
    R, s = signature
    Q = public_key
    
    # Calculate e = H(R || Q || m)
    e = hash_point_message(R, Q, message)
    
    # Check if sG = R + eQ
    left = s * ec.G
    right = R + e * Q
    
    return left == right 