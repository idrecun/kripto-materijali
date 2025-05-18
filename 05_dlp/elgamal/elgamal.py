import diffie_hellman as dh

# Encodes a string into an integer
def encode(message):
    return int(message.encode('utf-8').hex(), 16)

# Decodes a string from an integer
def decode(message):
    return bytes.fromhex(hex(message)[2:]).decode('utf-8')

def encrypt(priv_key, oth_pub_key, message):
    S = dh.shared_key(priv_key, oth_pub_key)
    return (message * S) % dh.p

def decrypt(priv_key, oth_pub_key, ciphertext):
    S = dh.shared_key(priv_key, oth_pub_key)
    return (ciphertext * pow(S, -1, dh.p)) % dh.p
