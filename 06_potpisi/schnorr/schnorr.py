"""
Schnorr digitalni potpisi.
"""

from hashlib import sha256
from random import randrange

# Testni Schnorr parametri
p = 0x86F5CA03DCFEB225063FF830A0C769B9DD9D6153AD91D7CE27F787C43278B447E6533B86B18BED6E8A48B784A14C252C5BE0DBF60B86D6385BD2F12FB763ED8873ABFD3F5BA2E0A8C0A59082EAC056935E529DAF7C610467899C77ADEDFC846C881870B7B19B2B58F9BE0521A17002E3BDD6B86685EE90B3D9A1B02B782B1779
q = 0x996F967F6C8E388D9E28D01E205FBA957A5698B1
g = 0x07B0F92546150B62514BB771E2A0C0CE387F03BDA6C56B505209FF25FD3C133D89BBCD97E904E09114D9A7DEFDEADFC9078EA544D2E401AEECC40BB9FBBF78FD87995A10A1C27CB7789B594BA7EFB5C4326A9FE59A070E136DB77175464ADCA417BE5DCE2F40D10A46A3A3943F26AB7FD9C0398FF8C76EE0A56826A8A88F1DBD

def generate():
    x = randrange(2, q)  # privatni ključ
    y = pow(g, x, p)     # javni ključ
    return x, y

def sign(private_key, message):
    x = private_key

    # Heširamo poruku
    h = int.from_bytes(sha256(message.encode()).digest(), 'big')

    while True:
        # Biramo slučajan broj k
        k = randrange(2, q)
        
        # Računamo r = g^k mod p
        r = pow(g, k, p)
        if r == 0:
            continue

        # Računamo e = H(r || m)
        e = hash_message(message, r)
        if e == 0:
            continue

        # Računamo s = k + xe mod q
        s = (k + x * e) % q
        if s == 0:
            continue

        return r, s

def verify(public_key, message, signature):
    y = public_key
    r, s = signature

    # Proveravamo da li je potpis u opsegu
    if not (0 < r < p and 0 < s < q):
        return False

    # Računamo e = H(r || m)
    e = hash_message(message, r)

    # Proveravamo da li je g^s = r * y^e mod p
    left = pow(g, s, p)
    right = (r * pow(y, e, p)) % p

    return left == right

def hash_message(message, r):
    """
    Heš funkcija koja kombinuje poruku i vrednost r.
    """
    h = sha256()
    h.update(str(r).encode())
    h.update(message.encode())
    return int.from_bytes(h.digest(), 'big') 