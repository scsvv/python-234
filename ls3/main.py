"""
# Выведите строку 'четное', если введенное число четно, и строку 'нечетное', если число нечетно.

number = input('Enter number: ')

if int(number)%2==0:
    print(f'Число {number} является четным')
else:
    print(f'Число {number} является нечетным')
"""

# Пользователь вводит два числа: координаты шахматной клетки.
# Выведите YES, если клетка белая, и NO, если - черная.


# x = int(input("Type x: "))
# y = int(input("Type y: "))

# if x < 1 or x > 8 or y < 1 or y > 8:
#     print("Error: not vaild data")
# elif (x+y)%2==0:
#     print('White')
# else:
#     print('Black')

import datetime
today = datetime.date.today()
print(today.strftime('%w'))
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

day = int(input('Type number of  the day: '))
if day > 0 and day < 6:
    print(f"{days[day-1]} is a work day")
elif day > 5 and day < 8:
    print(f"{days[day-1]} is a holiday")
else:
    print("Are you sure?")
