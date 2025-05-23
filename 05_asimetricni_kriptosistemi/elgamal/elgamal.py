import diffie_hellman as dh

def encrypt(priv_key, oth_pub_key, message):
    S = dh.shared_key(priv_key, oth_pub_key)
    return (message * S) % dh.p

def decrypt(priv_key, oth_pub_key, ciphertext):
    S = dh.shared_key(priv_key, oth_pub_key)
    return (ciphertext * pow(S, -1, dh.p)) % dh.p
