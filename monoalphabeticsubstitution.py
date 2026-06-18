"""
Each letter in the alphabet is mapped to a unique substitute letter.
"""

import random
import string


def generate_key() -> dict:
  
    alphabet = list(string.ascii_lowercase)
    shuffled = alphabet.copy()
    random.shuffle(shuffled)
    return dict(zip(alphabet, shuffled))


def invert_key(key: dict) -> dict:

    return {v: k for k, v in key.items()}


def encode(plaintext: str, key: dict) -> str:

    result = []
    for char in plaintext:
        if char.lower() in key:
            substituted = key[char.lower()]

            result.append(substituted.upper() if char.isupper() else substituted)
        else:
            result.append(char)  
    return "".join(result)


def decode(ciphertext: str, key: dict) -> str:

    decode_key = invert_key(key)
    return encode(ciphertext, decode_key)


def display_key(key: dict) -> None:

    print("\n🔑 Substitution Key:")
    print("  Plain :  " + " ".join(key.keys()).upper())
    print("  Cipher:  " + " ".join(key.values()).upper())


def key_to_string(key: dict) -> str:

    return "".join(key[c] for c in string.ascii_lowercase)


def key_from_string(key_str: str) -> dict:

    if len(key_str) != 26:
        raise ValueError("Key string must be exactly 26 characters.")
    key_str = key_str.lower()
    if len(set(key_str)) != 26:
        raise ValueError("Key string must contain each letter exactly once.")
    return dict(zip(string.ascii_lowercase, key_str))

if __name__ == "__main__":
    print("=" * 55)
    print("   Monoalphabetic Substitution Cipher Demo")
    print("=" * 55)

    key = generate_key()
    display_key(key)

    message = "Hello, Roblox World! Adopt Me is the best game."
    print(f"\n📝 Original Message:\n   {message}")

    ciphertext = encode(message, key)
    print(f"\n🔒 Encoded Message:\n   {ciphertext}")

    decoded = decode(ciphertext, key)
    print(f"\n🔓 Decoded Message:\n   {decoded}")

    print(f"\n✅ Round-trip match: {message == decoded}")

    key_str = key_to_string(key)
    print(f"\n📦 Serialized Key (save this!):\n   {key_str}")

    print("\n" + "=" * 55)
    print("   Custom Key Example")
    print("=" * 55)
    custom_key_str = "zyxwvutsrqponmlkjihgfedcba"  
    custom_key = key_from_string(custom_key_str)
    display_key(custom_key)

    sample = "The quick brown fox jumps over the lazy dog."
    encoded = encode(sample, custom_key)
    decoded2 = decode(encoded, custom_key)
    print(f"\n📝 Original : {sample}")
    print(f"🔒 Encoded  : {encoded}")
    print(f"🔓 Decoded  : {decoded2}")
    print(f"✅ Match    : {sample == decoded2}")

    print("\n" + "=" * 55)
    print("   Interactive Mode")
    print("=" * 55)
    print("Using the randomly generated key from above.\n")

    while True:
        choice = input("Choose action — (E)ncode / (D)ecode / (Q)uit: ").strip().upper()
        if choice == "Q":
            print("Goodbye!")
            break
        elif choice == "E":
            text = input("Enter text to encode: ")
            print(f"Encoded: {encode(text, key)}\n")
        elif choice == "D":
            text = input("Enter text to decode: ")
            print(f"Decoded: {decode(text, key)}\n")
        else:
            print("Invalid choice. Please enter E, D, or Q.\n")
