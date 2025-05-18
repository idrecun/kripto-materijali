import random
from hashlib import sha256

def generate_keys(p, g):
    """Generate public and private keys for ElGamal signature."""
    x = random.randint(1, p-2)  # Private key
    y = pow(g, x, p)            # Public key
    return (p, g, y), x

def sign_message(p, g, x, message):
    """Sign a message using the private key."""
    while True:
        k = random.randint(1, p-2)
        if gcd(k, p-1) == 1:  # k must be coprime to p-1
            break
    print("random k:", k)
    r = pow(g, k, p)
    k_inv = pow(k, -1, p-1)
    h = int(sha256(message.encode()).hexdigest(), 16)
    s = (k_inv * (h + x * r)) % (p-1)
    return (r, s)

def verify_signature(p, g, y, message, r, s):
    """Verify a message signature using the public key."""
    if not (0 < r < p):
        return False
    if not (0 < s < p-1):
        return False
    h = int(sha256(message.encode()).hexdigest(), 16)
    v1 = (pow(g, h, p) * pow(y, r, p)) % p
    v2 = pow(r, s, p)
    return v1 == v2

def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return a

# Example usage:
# p = 467  # A prime number
# g = 2    # A primitive root modulo p
g, p = [int(x) for x in input().split()]

# Generate keys
public_key, private_key = generate_keys(p, g)
print("Public Key:", public_key)
print("Private Key:", private_key)

# Sign a message
message = "Hello, ElGamal!"
signature = sign_message(p, g, private_key, message)
print("Signature:", signature)

# Verify the signature
is_valid = verify_signature(p, g, public_key[2], message, signature[0], signature[1])
print("Signature valid:", is_valid)

