import sys


def xor_bytes(bytes1, bytes2):
    return bytes(x ^ y for x, y in zip(bytes1, bytes2))


def load_dictionary():
    # Load the dictionary from "dictionary.txt" into a set
    with open("dictionary.txt", "r") as dictionary_file:
        dictionary = set(word.strip().lower() for word in dictionary_file)
    return dictionary


def analyze_segment(segment, dictionary):
    try:
        # Convert the hex string segment back to regular text
        text_segment = segment.decode("ascii")

        # Split the text into words, ignoring whitespaces, commas, etc.
        words = [word.strip(".,;?!") for word in text_segment.split()]

        # Check if any word in the segment exists in the dictionary
        for word in words:
            if word.lower() in dictionary:
                return text_segment  # Successful analysis

        return ""  # Analysis failed

    except:
        return ""


def decrypt_attempt(ciphertext, ciphertext1, ciphertext2, word, dictionary):
    word_bytes = word.encode("ascii")
    word_length = len(word_bytes)
    ciphertext_length = len(ciphertext)

    for i in range(ciphertext_length - word_length + 1):
        segment = ciphertext[i : i + word_length]
        xor_result = xor_bytes(segment, word_bytes)
        xor_text = analyze_segment(xor_result, dictionary)

        if xor_text != "":
            print(
                f"Possible decryption found on segment [{i}, {i + word_length}]: {xor_text}"
            )

            segment1 = ciphertext1[i : i + word_length]
            segment2 = ciphertext2[i : i + word_length]

            key_segment1 = xor_bytes(segment1, word_bytes)
            key_segment2 = xor_bytes(segment2, word_bytes)

            try:
                segment_text1 = key_segment1.decode("ascii")
                print(f"Possible key segment: {segment_text1}")
            except:
                pass

            try:
                segment_text2 = key_segment2.decode("ascii")
                print(f"Possible key segment: {segment_text2}")
            except:
                pass


if len(sys.argv) != 3:
    print("Usage: python script.py file1.txt file2.txt")
    sys.exit(1)

file1_path = sys.argv[1]
file2_path = sys.argv[2]

hex_text1 = ""
hex_text2 = ""

with open(file1_path, "r") as file1, open(file2_path, "r") as file2:
    hex_text1 = file1.read().strip()
    hex_text2 = file2.read().strip()

bytes1 = bytes.fromhex(hex_text1)
bytes2 = bytes.fromhex(hex_text2)

result = xor_bytes(bytes1, bytes2)

dictionary = load_dictionary()

for word in dictionary:
    print(f"Searching for word '{word}' ...")
    decrypt_attempt(result, bytes1, bytes2, word, dictionary)
    print("")
