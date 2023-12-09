numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
k = 12
numbers_set = set()
for number in numbers:
    basis = k - number
    if basis in numbers_set:
        print(f'{number} + {basis} = {k}')
        break
    else:
        numbers_set.add(number)
