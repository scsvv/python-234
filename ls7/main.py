numbers = list([1, 2, 3, 4, 5, 6, 'a', 7, 8, 9])
print(f'\nFirst state:\t{numbers}\n')

# append
numbers.append(10)
numbers.append(11)
numbers.append(12)

print(f'Second state:\t{numbers}\n')

# insert
# numbers.insert(0, 'a')
# numbers.insert(1, 'b')

# print(f'Third state:\t\t{numbers}\n')

# # reverse
# numbers.reverse()
# print(f'Revers third state: \t{numbers}\n')

# remove
numbers.remove('a')
print(f'remove state:\t{numbers}')
numbers.remove(5)
print(f'remove state:\t{numbers}')

# pop
numbers.pop(0)
print(f'pop state:\t{numbers}')
numbers.pop()
print(f'pop state:\t{numbers}')
