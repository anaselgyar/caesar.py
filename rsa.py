from Crypto.Util.number import *  

# parameters
p = getPrime(1024)
q = getPrime(1024)
n = p * q              # public field
ph = (p-1) * (q-1)    # private field
e = (2**16)+1          
d = pow(e, -1, ph)

PT = bytes_to_long(b"hello world")
CT = pow(PT, e, n)
decrypted = long_to_bytes(pow(CT, d, n))

# demo
print(f"plaintext: {PT}")
print(f"ciphertext: {CT}")      
print(f"decrypted: {decrypted}")       