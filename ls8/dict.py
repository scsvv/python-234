"""
"Пора учить английский язык", - сказал себе Степа и решил написать программу для изучения английского языка. Программа получает на вход слово на английском языке и несколько его переводов на русском языке. Составьте словарь, в котором ключ - это английское слово, а значение - это список русских слов. В этой задаче нужно использовать строчный метод split()."""
# import re

# vocabulary = dict()

# while True:
#     data = input("Type your words: english - another languages: ")
#     if data == "1":
#         print(vocabulary)
#         exit()

#     data = data.split(":")
#     if len(data) != 2:
#         exit()

#     vocabulary.setdefault(data[0].replace(" ", ""), data[1].replace(" ", ""))
#     vocabulary[data[0].replace(" ", "")] = data[1].replace(" ", "")

# user = {
#     "name": "NAME",
#     "age": 12,
# }

# print(user.get("name"))
# print(user["name"])

# print(user.get("r"))
# # print(user["r"])

# list_of_words = ['hello', 'hello', 'hi']
# words = {}

# for word in list_of_words:
#     words[word] = words.get(word, 0) + 1

# # Функция max может получать функцию в качестве второго аргумента
# freq_word = max(words, key=words.get)

# print(freq_word)

# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age. Найдите самого младшего из друзей и выведите его имя.

try:
    N = input("Type N: ")
    N = int(N)
    if N == 0 or N < 0:
        raise ValueError()
except ValueError:
    print("Fatal Error: Invalid Data")
    exit()

friends = list()

for i in range(N):
    name = input("Enter name: ")
    age = input("Enter age: ")

    try:
        age = int(age)
    except ValueError:
        age = None

    friends.append(dict(name=name, age=age, id=i))

print(friends)
mf = friends[0]

for friend in friends[1::]:
    if friend.get("age") > mf.get("age"):
        mf = friend

print(mf)
