text = input('Enter your text:')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = int(input('Enter your cipher key:'))

def encryption(text, key):
    text = text.lower()
    ciphertext = ""

    for letter in text:
        ciphertext += alphabet[(alphabet.index(letter) + key ) %26]

    return ciphertext
ciphertext = encryption(text, key)


def decryption(ciphertext, key):
    ciphertext = ciphertext.lower()
    text = ""

    for letter in ciphertext:
        text += alphabet[(alphabet.index(letter) - key ) %26]

    return text
decrypeted = decryption(ciphertext, key)

print(f"your encryption text is: {ciphertext}")
print(f"your decryption text is: {decrypeted}")
