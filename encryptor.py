def xor_encrypt(data: str, key: bytes):
    encrypted = bytearray()
    for i, char in enumerate(data.encode()):
        encrypted.append(char ^ key[i % len(key)])
    return encrypted

def xor_decrypt(enc: bytearray, key: bytes):
    decrypted = bytearray()
    for i, byte in enumerate(enc):
        decrypted.append(byte ^ key[i % len(key)])
    return decrypted.decode()
