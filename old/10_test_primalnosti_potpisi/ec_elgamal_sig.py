import random
from hashlib import sha256
import ec  # Assuming `ec` is the elliptic curve library

def generate_keys(curve):
    """Generate public and private keys for ElGamal signature using elliptic curves."""
    private_key = random.randint(1, curve.n - 1)  # Private key
    public_key = private_key * curve.G            # Public key (G is the base point)
    return public_key, private_key

def sign_message(curve, private_key, message):
    """Sign a message using the private key."""
    while True:
        k = random.randint(1, curve.n - 1)
        if k % curve.n != 0:  # k must be non-zero and less than n
            break
    r_point = k * curve.G
    r = r_point.x % curve.n
    k_inv = pow(k, -1, curve.n)
    h = int(sha256(message.encode()).hexdigest(), 16) % curve.n
    s = (k_inv * (h + private_key * r)) % curve.n
    return (r, s)

def verify_signature(curve, public_key, message, r, s):
    """Verify a message signature using the public key."""
    if not (1 <= r < curve.n):
        return False
    if not (1 <= s < curve.n):
        return False
    h = int(sha256(message.encode()).hexdigest(), 16) % curve.n
    w = pow(s, -1, curve.n)
    u1 = (h * w) % curve.n
    u2 = (r * w) % curve.n
    point = u1 * curve.G + u2 * public_key
    return (point.x % curve.n) == r

# Example usage:
curve = ec.get_curve('secp256k1')  # Example curve, e.g., secp256k1

# Generate keys
public_key, private_key = generate_keys(curve)
print("Public Key:", public_key)
print("Private Key:", private_key)

# Sign a message
message = "Hello, ElGamal with Elliptic Curves!"
signature = sign_message(curve, private_key, message)
print("Signature:", signature)

# Verify the signature
is_valid = verify_signature(curve, public_key, message, signature[0], signature[1])
print("Signature valid:", is_valid)

