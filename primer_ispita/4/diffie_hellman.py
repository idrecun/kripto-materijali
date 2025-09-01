import secrets
from ec import G, secp256k1


def private_key():
    # TODO: Implement ECDH private key
    return secrets.randbelow(secp256k1.n - 1) + 1


def public_key(priv):
    # TODO: Implement ECDH public key
    return priv * G


def shared_key(priv, pub):
    # TODO: Implement ECDH shared key
    return priv * pub


