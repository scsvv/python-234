# NUMBERS = [1, 3, 4, 5, 6], K = 9

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
k = 12

numbers_set = set()
for number in numbers:
    basis = k - number
    # Python
    # if numbers.count(basis) != 0:
    #     print(f'{number} + {basis} = {k}')
    #     break

    # Algorytms -> N
    print(number, basis, numbers_set, number is numbers_set)
    if basis in numbers_set:
        print(f'{number} + {basis} = {k}')
        break
    else:
        numbers_set.add(number)

print(numbers_set)
print("Exit")
