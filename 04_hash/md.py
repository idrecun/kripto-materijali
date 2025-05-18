# Implements a simple MD constructed hash
from bits import (
    xor,
    bits_from_blocks,
    bits_from_string,
    bits_to_blocks,
    bits_to_hex,
    bits_from_int,
)
import spn

block_size = 32
f = spn.new(2 * block_size, block_size)


def pad(b, block_size):
    pad_len = block_size - (len(b) + 2) % block_size
    return b + [1] + [0] * (pad_len - 2) + [1]


def md(data):
    padded = pad(data, block_size)
    state = [0] * block_size  # IV
    for block in bits_to_blocks(padded, block_size):
        state = f(bits_from_blocks([state, block]))
    return state


def hmac(key, message):
    opad = bits_from_int(0x36, 8) * len(message // 8)
    ipad = bits_from_int(0x5C, 8) * len(message // 8)
    return md(xor(opad, key) + md(xor(ipad, key) + message))


def kdf(password, length):
    blocks = [
        md(password + bits_from_int(i, 64)) for i in range(1 + length // block_size)
    ]
    return bits_from_blocks(blocks)[:length]


data = bits_from_string(input())
hash = md(data)
print(bits_to_hex(hash))
