# -> uniq ? -> 

from random import randint

numbers = list()
N = 10

for i in range(N):
    numbers.append(randint(1, 4))

unumbers = list()

for number in numbers:
    if unumbers.count(number) == 0:
        unumbers.append(number)

numbers_set = set(numbers)

for i in range(N):
    numbers_set.add(randint(0, 5))
    numbers.append(randint(0, 5))



print(numbers)
print(unumbers)
print(numbers_set)