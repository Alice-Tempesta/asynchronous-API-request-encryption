import secrets
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode

def generate_key():
    return secrets.token_bytes(32)

def aes_encrypt(message, key):
    key = key.ljust(32)
    key = key[:32]
    
    iv = secrets.token_bytes(16)
    
    # Оставляем текст в байтовом виде так как вызывает ошибку кодировки, хрен пойми почему
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    ciphertext = encryptor.update(message) + encryptor.finalize()
    return b64encode(iv + ciphertext)

def aes_decrypt(ciphertext, key):
    key = key.ljust(32)
    key = key[:32]
    
    ciphertext = b64decode(ciphertext)
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]
    
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext
