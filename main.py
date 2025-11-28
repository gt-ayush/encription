from .keygen import generate_key
from .encryptor import xor_encrypt, xor_decrypt
def run():
    text = input("Enter text to encrypt: ")

    key = generate_key()
    encrypted = xor_encrypt(text, key)
    decrypted = xor_decrypt(encrypted, key)

    print("\n🔐 Encrypted:", encrypted)
    print("🔓 Decrypted:", decrypted)

if __name__ == "__main__":
    run()
