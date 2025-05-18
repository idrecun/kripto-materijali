from sympy import Matrix


def lfsr_break(output_bits, lfsr_length):
    if len(output_bits) < 2 * lfsr_length:
        raise ValueError("Insufficient output bits.")

    # Build the matrix and output vector
    matrix = Matrix([output_bits[i : i + lfsr_length] for i in range(lfsr_length)])
    output_vector = Matrix(output_bits[lfsr_length : lfsr_length * 2])

    # Solve for feedback taps in GF(2)
    taps = (matrix.inv_mod(2) * output_vector) % 2
    initial_state = output_bits[:lfsr_length]

    return taps, initial_state


# Example usage
output_bits = [1, 0, 0, 1, 0, 0, 0, 1, 1, 1]
lfsr_length = 4
taps, initial_state = lfsr_break(output_bits, lfsr_length)
print("Recovered taps:", taps)
print("Recovered initial state:", initial_state)
