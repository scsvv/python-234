
# Создайте список из 10 четных чисел и выведите его с помощью цикла for
from random import randint

numbers = list()

for i in range(10):
    a = randint(0, 10)
    if a % 2 != 0:
        a += 1
    numbers.append(a)  # add new element in the end

for number in numbers:
    print(number)

# numbers.clean()
for i in range(len(numbers)):
    numbers.pop()

print(numbers)
