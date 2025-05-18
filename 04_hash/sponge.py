# Implements a sponge constructed hash function
from bits import (
    xor,
    bits_to_blocks,
    bits_from_blocks,
    bits_from_string,
    bits_to_hex,
)
import spn

r = 64
c = 128
f = spn.new(r + c, r + c)


def absorb(state, block, f):
    absorbed = xor(state[:r], block) + state[r:]
    return f(absorbed)


def squeeze(state, f):
    return f(state), state[:r]


def pad(data):
    global r
    pad_size = r - (len(data) + 2) % r
    return data + [1] + [0] * (pad_size - 2) + [1]


def sponge(data, output_blocks):
    blocks = bits_to_blocks(pad(data), r)
    state = [0] * (r + c)
    for block in blocks:
        state = absorb(state, block, f)
    hash = []
    for _ in range(output_blocks):
        state, output = squeeze(state, f)
        hash.append(output)
    return bits_from_blocks(hash)


def mac(key, message):
    return sponge(key + message, 1)


def kdf(password):
    return sponge(password, 1)


data = bits_from_string(input())
hash = sponge(data, 1)
print(bits_to_hex(hash))
