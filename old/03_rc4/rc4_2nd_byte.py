from getpass import getpass
import random
from string import ascii_lowercase

# Key scheduling algorithm
def KSA(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256   # j += S[i] + K[i]
        S[i], S[j] = S[j], S[i]                      # swap(S[i], K[i])
    return S

# Pseudo-random generation algorithm
def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256            # i += 1
        j = (j + S[i]) % 256         # j += S[i]
        S[i], S[j] = S[j], S[i]      # swap(S[i], S[j])
        K = S[(S[i] + S[j]) % 256]   # K = S[S[i] + S[j]]
        yield K

tests = 0
zeros = 0
while True:
    tests += 1
    key = [ord(random.choice(ascii_lowercase)) for _ in range(10)]
    S = KSA(key)
    keystream = PRGA(S)
    K = next(keystream)
    K = next(keystream)
    if K == 0:
        zeros += 1

    if tests % 10000 == 0:
        print('\r', end='')
        print('Expected: ', tests // 256, '; Counter: ', zeros, end='')

