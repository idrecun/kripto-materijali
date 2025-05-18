# Implements symmetric cryptography primitives
from bits import bits_to_int, bits_from_int


def pbox(input_bits, permutation):
    permuted_bits = [input_bits[i - 1] for i in permutation]
    return permuted_bits


def sbox(input_bits, substitution_table):
    input_value = bits_to_int(input_bits)
    substituted_value = substitution_table[input_value]
    return bits_from_int(substituted_value, 4)


# Example usage
input_bits = [1, 0, 1, 0, 1, 1, 0, 0]
permutation = [3, 1, 4, 2, 5, 7, 6, 8]
print("P-Box Output:", pbox(input_bits, permutation))

# Example usage
input_bits = [1, 0, 1, 0]
substitution_table = {
    0: 14,
    1: 4,
    2: 13,
    3: 1,
    4: 2,
    5: 15,
    6: 11,
    7: 8,
    8: 3,
    9: 10,
    10: 6,
    11: 12,
    12: 5,
    13: 9,
    14: 0,
    15: 7,
}
print("S-Box Output:", sbox(input_bits, substitution_table))
