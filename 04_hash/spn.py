import random

from bits import bits_to_blocks, bits_from_int, bits_to_int, bits_from_blocks, xor


def permute(state, p):
    return [state[i] for i in p]


def substitute(state, s):
    blocks = bits_to_blocks(state, 8)
    subs = [
        bits_from_int(s[i][bits_to_int(block)], 8) for (i, block) in enumerate(blocks)
    ]
    return bits_from_blocks(subs)


def new(input_bits, output_bits):
    rounds = 4
    random.seed(123)
    p = random.sample(list(range(input_bits)), input_bits)
    s = [random.sample(list(range(256)), 256) for _ in range(input_bits // 8)]
    k = [random.choices([0, 1], k=input_bits) for _ in range(rounds)]

    def f(state):
        t = state[:]
        for i in range(rounds):
            t = substitute(t, s)
            t = permute(t, p)
            t = xor(t, k[i])
        return t[:output_bits]

    return f
