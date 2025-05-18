# Stream cipher based on LFSR
from lfsr import lfsr_run
from bits import bits_from_string, bits_to_string, bits_to_bitstring, xor


def stream_cipher(text_bits, password):
    taps = [3, 31]
    seed = bits_from_string(password)[:32]
    lfsr_gen = lfsr_run(seed, taps)
    keystream = [next(lfsr_gen) for _ in range(len(text_bits))]
    return xor(text_bits, keystream)


# Example usage
if __name__ == "__main__":
    plaintext = "Hello, World!"
    password = "secret"

    plaintext_bits = bits_from_string(plaintext)

    # Encrypt
    ciphertext = stream_cipher(plaintext_bits, password)
    print("Ciphertext:", bits_to_bitstring(ciphertext))

    # Decrypt
    decrypted_bits = stream_cipher(ciphertext, password)
    decrypted_text = bits_to_string(decrypted_bits)
    print("Decrypted text:", decrypted_text)
