# gen list -> max min; 3 -> im | im -> p | p

from random import randint

numbers = list()

for i in range(100):
    numbers.append(randint(-1000, 1000))

print(numbers)

max_value, min_value = numbers[0], numbers[0]

for number in numbers:
    if number > max_value:
        max_value = number
    elif number < min_value:
        min_value = number

print(min_value, max_value)

numbers.sort()
print(numbers[0], numbers[len(numbers)-1])

print(min(numbers), max(numbers))
