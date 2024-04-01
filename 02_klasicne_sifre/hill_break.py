from sympy import Matrix, symbols, solve
from math import isqrt
from string import ascii_lowercase
from getpass import getpass

Mod = 26

m = input('Enter message:')
c = input('Enter ciphertext:')
n = 2

m_encoded = [ascii_lowercase.index(ch) for ch in m]
c_encoded = [ascii_lowercase.index(ch) for ch in c]

M = Matrix([[m_encoded[0], m_encoded[2]],
            [m_encoded[1], m_encoded[3]]])
C = Matrix([[c_encoded[0], c_encoded[2]],
            [c_encoded[1], c_encoded[3]]])

# C = KM
# K = CM^-1

M = M.inv_mod(Mod)
K = (C * M) % Mod

K_encoded = K.tolist()
k_encoded = [K_encoded[0][0], K_encoded[0][1], K_encoded[1][0], K_encoded[1][1]]

k = ''.join(ascii_lowercase[ch] for ch in k_encoded)

print(k)
