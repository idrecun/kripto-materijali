import random
from hashlib import sha256

def mod_inverse(a, m):
    """Find the modular inverse of a under modulo m using Extended Euclidean Algorithm."""
    return pow(a, -1, m)

def generate_keys(p, g):
    """Generate public and private keys for Schnorr signature using prime field."""
    private_key = random.randint(1, p-2)  # Private key
    public_key = pow(g, -private_key, p)  # Public key
    return public_key, private_key

def sign_message(p, g, private_key, message):
    """Sign a message using the private key."""
    k = random.randint(1, p-2)
    r = pow(g, k, p)
    h = int(sha256((str(r) + message).encode()).hexdigest(), 16) % p
    s = (k + h * private_key) % (p-1)
    return (r, s)

def verify_signature(p, g, public_key, message, r, s):
    """Verify a message signature using the public key."""
    if not (0 < r < p):
        return False
    if not (0 < s < p-1):
        return False
    h = int(sha256((str(r) + message).encode()).hexdigest(), 16) % p
    lhs = (pow(g, s, p) * pow(public_key, h, p)) % p
    rhs = r
    return lhs == rhs

# Example usage:
p = 467  # A prime number, typically this would be a large prime
g = 2    # A generator of the multiplicative group of integers modulo p

# Generate keys
public_key, private_key = generate_keys(p, g)
print("Public Key:", public_key)
print("Private Key:", private_key)

# Sign a message
message = "Hello, Schnorr's signature with prime field!"
signature = sign_message(p, g, private_key, message)
print("Signature:", signature)

# Verify the signature
is_valid = verify_signature(p, g, public_key, message, signature[0], signature[1])
print("Signature valid:", is_valid)

