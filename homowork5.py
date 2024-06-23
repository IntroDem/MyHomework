# Необходимо найти в коде ошибку. На данный момент эта функция удаляет только последнее слово из текста.
# Нужно сделать чтобы все слова удалялись из текста.
# def censure(text, censured_words):
#     new_text = ""
#     for word in censured_words:
#         start_index = text.find(word)
#         end_index = start_index + len(word)
#
#         if text.find(word) != -1:
#             firs_section = text[:start_index]
#             second_section = text[end_index:]
#             new_text = firs_section + second_section
#
#     return new_text
# Переменная new_txt каждый раз перезаписывается и и в итоге только последнее удаление остаётся в готовом тексте.
# Нужно обновлять текст каждый раз при удалении слова. Поместить в цикл.

string = "Lorem amet ipsum dolor sit amet consectetur dolor adipiscing elit. Donec amet eiusmod tempor amet nec aliqua."


def censure(text, censure_words):
    new_text = text
    for word in censure_words:
        while word in new_text:
            start_index = new_text.find(word)
            end_index = start_index + len(word)
            new_text = new_text[:start_index] + new_text[end_index:]
    return new_text


print(string)
print(censure(string, ["amet", "dolor"]))


# Задание 1
# Пользователь вводит с клавиатуры некоторый текст, после чего пользователь вводит список зарезервированных слов.
# Необходимо найти в тексте все зарезервированные слова и изменить их регистр на верхний.
# Вывести на экран измененный текст.

input_text = input("Enter a string: ")
input_reserved_words = input("Enter a set of words: ")
reserved_words = input_reserved_words.split()

for word in reserved_words:
    input_text = input_text.replace(word, word.upper())

print("Modified text:", input_text)

# Задание 2
# Есть некоторый текст. Посчитайте в этом тексте количество предложений и выведите на экран полученный результат.
some_text = (
    "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the "
    "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type "
    "and scrambled it to make a type specimen book. It has survived not only five centuries, but also the "
    "leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with "
    "the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing"
    " software like Aldus PageMaker including versions of Lorem Ipsum."
)

import re


def count_sentences(text):

    end_sentence = re.compile(r"[.!?]+")

    sentences = end_sentence.split(text)
    sentences = list(filter(str.strip, sentences))
    num_sentences = len(sentences)
    return num_sentences


sentence_count = count_sentences(some_text)
print("Количество предложений:", sentence_count)
