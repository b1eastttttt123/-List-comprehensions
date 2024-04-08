def caesar_cipher(message, shift):
    encrypted_message = ""
    for letter in message:
        if letter.isalpha():
            if letter.islower():
                encrypted_message += chr((ord(letter) - ord('а') + shift) % 32 + ord('а'))
            elif letter.isupper():
                encrypted_message += chr((ord(letter) - ord('А') + shift) % 32 + ord('А'))
        else:
            encrypted_message += letter
    return encrypted_message

message = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))

encrypted_message = caesar_cipher(message, shift)

print("Зашифрованное сообщение:", encrypted_message)
