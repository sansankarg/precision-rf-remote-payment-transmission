from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from base64 import b64encode, b64decode

def aes_encrypt(key, iv, plaintext):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return b64encode(ciphertext).decode()

def aes_decrypt(key, iv, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(b64decode(ciphertext)) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    unpadded_plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return unpadded_plaintext.decode()

cipher_key = bytes([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
cipher_iv = bytes([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

plaintext = "82207091316381998286100000"
ciphertext = aes_encrypt(cipher_key, cipher_iv, plaintext)
print(ciphertext)
#
# decrypted_text = aes_decrypt(cipher_key, cipher_iv, ciphertext)
# print(decrypted_text)
