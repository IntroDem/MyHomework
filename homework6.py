# Задание: Шифровка и дешифровка сообщения
# В предметной области шифрования и дешифровки сообщений необходимо написать программу, которая выполняет следующие
# операции:
# На вход программы поступает исходное сообщение в виде строки.
# Программа шифрует сообщение путем замены каждой буквы на следующую в алфавите. Например, 'a' становится 'b', 'b'
# становится 'c', ..., 'z' становится 'a'.
# Шифрованное сообщение выводится на экран.
# Затем программа предлагает пользователю ввести шифрованное сообщение для дешифровки.
# Программа дешифрует сообщение, заменяя каждую букву на предыдущую в алфавите.
# Дешифрованное сообщение выводится на экран.
#
# Пример работы программы:
# Введите исходное сообщение: python
# Зашифрованное сообщение: qzuipo
# Введите зашифрованное сообщение для дешифровки: qzuipo
# Дешифрованное сообщение: python
#
# P.S. Для решения необходимы функции ord() и chr(). ord() – позволяет получить код символа, chr() – позволяет получит
# символ по коду.

default_mess = input("Введите сообщение для шифрования: ")


def encrypt_mess(mess):
    encrypted_mess = ""
    for char in mess:
        if "А" <= char <= "Я":
            if char == "Я":
                encrypted_mess += "А"
            else:
                encrypted_mess += chr(ord(char) + 1)
        elif "а" <= char <= "я":
            if char == "я":
                encrypted_mess += "а"
            else:
                encrypted_mess += chr(ord(char) + 1)
        elif "A" <= char <= "Z":
            if char == "Z":
                encrypted_mess += "A"
            else:
                encrypted_mess += chr(ord(char) + 1)
        elif "a" <= char <= "z":
            if char == "z":
                encrypted_mess += "a"
            else:
                encrypted_mess += chr(ord(char) + 1)
        else:
            encrypted_mess += char
    return encrypted_mess


encrypted_mess = encrypt_mess(default_mess)
print("Зашифрованное сообщение: ", encrypted_mess)


encrypted_message_for_decryption = input(
    "Введите зашифрованное сообщение для расшифровки: "
)


def decrypt_mess(mess):
    decrypted_mess = ""
    for char in mess:
        if "А" <= char <= "Я":
            if char == "А":
                decrypted_mess += "Я"
            else:
                decrypted_mess += chr(ord(char) - 1)
        elif "а" <= char <= "я":
            if char == "а":
                decrypted_mess += "я"
            else:
                decrypted_mess += chr(ord(char) - 1)
        elif "A" <= char <= "Z":
            if char == "A":
                decrypted_mess += "Z"
            else:
                decrypted_mess += chr(ord(char) - 1)
        elif "a" <= char <= "z":
            if char == "a":
                decrypted_mess += "z"
            else:
                decrypted_mess += chr(ord(char) - 1)
        else:
            decrypted_mess += char
    return decrypted_mess


decrypted_mess = decrypt_mess(encrypted_message_for_decryption)
print("Расшифрованное сообщение: ", decrypted_mess)
