import secrets
import ec

# Generate a random private key
def private_key():
    return secrets.randbelow(ec.secp256k1.n - 2) + 1

# Calculate the public key
def public_key(a):
    return a * ec.G

# Calculate the shared secret key
def shared_key(a, B):
    return a * B
