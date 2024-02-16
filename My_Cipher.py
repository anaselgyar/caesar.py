from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

# Generated key
password = "copra"
salt = os.urandom(16)  
Aes_key = PBKDF2(password, salt, 32)  
iv = get_random_bytes(16)  # Generated IV
message = "Hello Secret World!"

# Encryption
cipher = AES.new(Aes_key, AES.MODE_CBC, iv)
ciphered_data = cipher.encrypt(pad(message.encode(), AES.block_size))

print(f"The Message: {message}")
print(f"The Ciphered Message: {ciphered_data}")