import sys


def lfsr_step(state, taps):
    feedback = 0
    for tap in taps:
        feedback ^= state[tap - 1]  # Convert 1-based index to 0-based
    output = state[-1]  # Output is the last bit of the state
    state = [feedback] + state[:-1]  # Shift left and insert feedback
    return state, output


def lfsr_run(seed, taps):
    state = seed[:]  # Initialize the LFSR state
    while True:
        state, output = lfsr_step(state, taps)
        yield int(output)


# Example usage
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python lfsr.py <bit_count>")
        sys.exit(1)

    bit_count = int(sys.argv[1])

    seed = [1, 0, 0, 1]  # Initial state
    taps = [1, 4]  # Tap positions (1-based index to match the C(X) polynomial)

    generator = lfsr_run(seed, taps)
    for _ in range(bit_count):
        print(next(generator), end="")
    print()
