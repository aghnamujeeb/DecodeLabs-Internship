def encrypt(msg, key):
    result=""
    for letter in msg:
        if letter.isupper():
            result+=chr((ord(letter) - ord('A') + key)%26+ord('A'))
        elif letter.islower():
            result+=chr((ord(letter) - ord('a') +key)%26 +ord('a'))
        else:
            result+=letter
    return result
def decrypt(msg, key):
    result2=""
    for letter in msg:
        if letter.isupper():
            result2+=chr((ord(letter) - ord('A') - key)%26+ord('A'))
        elif letter.islower():
            result2+=chr((ord(letter)-ord('a')-key)%26 +ord('a'))
        else:
            result2+=letter
    return result2
user_text=input("Enter text to encrypt: ")
encrypt_key= int(input("Enter shift to encrypt: "))
cipher_text = encrypt(user_text, encrypt_key)
print("Encrypted: ", cipher_text)
user_input=input("Enter text to decrypt: ")
decrypt_key=int(input("Enter shift to decrypt: "))
normal_text=decrypt(user_input, decrypt_key)
print("Decrypted: ", normal_text)