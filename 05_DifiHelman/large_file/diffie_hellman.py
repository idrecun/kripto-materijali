import secrets

# Diffie-Hellman 512-bit parameters
p_str = '0x\
      FFFFFFFF FFFFFFFF C90FDAA2 2168C234 C4C6628B 80DC1CD1\
      29024E08 8A67CC74 020BBEA6 3B139B22 514A0879 8E3404DD\
      EF9519B3 CD3A431B 302B0A6D F25F1437 4FE1356D 6D51C245\
      E485B576 625E7EC6 F44C42E9 A637ED6B 0BFF5CB6 F406B7ED\
      EE386BFB 5A899FA5 AE9F2411 7C4B1FE6 49286651 ECE45B3D\
      C2007CB8 A163BF05 98DA4836 1C55D39A 69163FA8 FD24CF5F\
      83655D23 DCA3AD96 1C62F356 208552BB 9ED52907 7096966D\
      670C354E 4ABC9804 F1746C08 CA237327 FFFFFFFF FFFFFFFF'
p = int(''.join(p_str.split()), 16)
g = 2

# Generate a random private key
def private_key():
    global p
    return secrets.randbelow(p - 2) + 1

# Calculate the public key
def public_key(a):
    global p, g
    return pow(g, a, p)

# Calculate the shared secret key
def shared_key(a, B):
    global p, g
    return pow(B, a, p)
