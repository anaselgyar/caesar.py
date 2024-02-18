ciphertext = input('Enter your text:')
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def decryption(ciphertext, key):
    ciphertext = ciphertext.lower()
    text = ""

    for letter in ciphertext:
        text += alphabet[(alphabet.index(letter) - key ) %26]

    return text

def brutforce(ciphertext):
    for key in range(0, 26):
        print(f"{key}: {decryption(ciphertext, key)}")

print(brutforce(ciphertext))
