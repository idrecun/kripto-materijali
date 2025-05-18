# Implements block cipher modes of operation
from bits import bits_to_blocks, bits_from_blocks, xor, bits_from_int


def ecb_mode(enc, data, block_size, key):
    blocks = bits_to_blocks(data, block_size)
    return bits_from_blocks(enc(block, key) for block in blocks)


def cbc_mode(enc, data, block_size, key, iv):
    blocks = bits_to_blocks(data, block_size)
    output, prev = [], iv
    for block in blocks:
        prev = enc(xor(block, prev), key)
        output.append(prev)
    return bits_from_blocks(output)


def ofb_mode(enc, data, block_size, key, iv):
    blocks = bits_to_blocks(data, block_size)
    output, stream = [], iv
    for block in blocks:
        stream = enc(stream, key)
        output.append(xor(block, stream))
    return bits_from_blocks(output)


def cfb_mode(enc, data, block_size, key, iv):
    blocks = bits_to_blocks(data, block_size)
    output, stream = [], iv
    for block in blocks:
        stream = xor(block, enc(stream, key))
        output.append(stream)
    return bits_from_blocks(output)


def ctr_mode(enc, data, block_size, key, nonce):
    blocks = bits_to_blocks(data, block_size)
    output = []
    for i, block in enumerate(blocks):
        stream = enc(bits_from_int(nonce + i, block_size), key)
        output.append(xor(block, stream))
    return bits_from_blocks(output)


plaintext = [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1]
key = [0, 1, 1, 0]

# Test all modes
print(ecb_mode(xor, plaintext, len(key), key))
print(ctr_mode(xor, plaintext, len(key), key, 0))
