from sympy import Matrix
from math import isqrt
from string import ascii_lowercase
from getpass import getpass

Mod = 26

m = input('Enter message:')
k = getpass('Enter key:')
n = isqrt(len(k))

if n ** 2 != len(k):
    print('Key length must be square')
    quit()

k_encoded = [ascii_lowercase.index(ch) for ch in k]
K = Matrix([k_encoded[i * n : (i + 1) * n] for i in range(n)])

try:
    K.inv_mod(Mod)
except:
    print('Matrix must be invertible')
    quit()

# Number of blocks to cover the whole message
num_blocks = (len(m) + n - 1) // n
print(num_blocks)

# Transform string into numbers mod 26 and pad message length to be divisible by n
m_encoded = [ascii_lowercase.index(ch) for ch in m]
m_encoded.extend([0] * (num_blocks * n - len(m)))
print(len(m_encoded))

# Split message into blocks
blocks = [m_encoded[i * n : (i + 1) * n] for i in range(num_blocks)]
print(len(blocks))

# Transform blocks into n-dimensional vectors
vectors = [ Matrix([[x] for x in block]) for block in blocks]
print(len(vectors))

# Encrypt each block
c_blocks = [(K * block) % Mod for block in vectors]
print(len(c_blocks))

# Unpack blocks into a list of numbers
c_encoded = [x for block in c_blocks for row in block.tolist() for x in row]
print(len(c_encoded))

# Back into string
c = "".join(ascii_lowercase[x] for x in c_encoded)

print(c)
