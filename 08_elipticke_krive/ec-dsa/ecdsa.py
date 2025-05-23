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

def sign(private_key, message):
    """
    Sign a message using EC-DSA.
    Returns (r, s) signature.
    """
    # Convert message to bytes and hash it
    h = int.from_bytes(sha256(message.encode()).digest(), 'big')
    
    while True:
        # Generate random k
        k = secrets.randbelow(ec.secp256k1.n - 2) + 1
        
        # Calculate R = kG and take x coordinate as r
        R = k * ec.G
        r = R.x % ec.secp256k1.n
        if r == 0:
            continue
            
        # Calculate s = k^(-1)(h + r*d) mod n
        s = (pow(k, -1, ec.secp256k1.n) * (h + r * private_key)) % ec.secp256k1.n
        if s == 0:
            continue
            
        return r, s

def verify(public_key, message, signature):
    """
    Verify an EC-DSA signature.
    """
    r, s = signature
    
    # Check if r and s are in [1, n-1]
    if not (0 < r < ec.secp256k1.n and 0 < s < ec.secp256k1.n):
        return False
    
    # Convert message to bytes and hash it
    h = int.from_bytes(sha256(message.encode()).digest(), 'big')
    
    # Calculate w = s^(-1) mod n
    w = pow(s, -1, ec.secp256k1.n)
    
    # Calculate u1 = hw mod n and u2 = rw mod n
    u1 = (h * w) % ec.secp256k1.n
    u2 = (r * w) % ec.secp256k1.n
    
    # Calculate R = u1*G + u2*Q
    R = u1 * ec.G + u2 * public_key
    
    # Check if R.x mod n equals r
    return R.x % ec.secp256k1.n == r 