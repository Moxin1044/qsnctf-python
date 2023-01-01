def caesar_encrypt(plaintext, shift):
    # 凯撒加密
    # 感谢OpenAI的大恩大德
    # Create an empty string to store the encrypted message.
    shift = int(shift)
    ciphertext = ""
    # Iterate over each character in the plaintext.
    for char in plaintext:
        # If the character is a letter, encrypt it using the Caesar cipher.
        if char.isalpha():
            # Shift the character by the specified shift value.
            shifted_char = chr(ord(char) + shift)
            # If the shifted character is not a letter, wrap it around.
            if not shifted_char.isalpha():
                shifted_char = chr(ord(shifted_char) - 26)
            # Add the encrypted character to the ciphertext.
            ciphertext += shifted_char
        # If the character is not a letter, add it to the ciphertext without encrypting it.
        else:
            ciphertext += char
    # Return the encrypted ciphertext.
    return ciphertext


def caesar_decrypt(ciphertext, shift):
    # 凯撒解密
    # Create an empty string to store the decrypted message.
    shift = int(shift)
    plaintext = ""
    # Iterate over each character in the ciphertext.
    for char in ciphertext:
        # If the character is a letter, decrypt it using the Caesar cipher.
        if char.isalpha():
            # Shift the character by the specified shift value.
            shifted_char = chr(ord(char) - shift)
            # If the shifted character is not a letter, wrap it around.
            if not shifted_char.isalpha():
                shifted_char = chr(ord(shifted_char) + 26)
            # Add the decrypted character to the plaintext.
            plaintext += shifted_char
        # If the character is not a letter, add it to the plaintext without decrypting it.
        else:
            plaintext += char
    # Return the decrypted plaintext.
    return plaintext