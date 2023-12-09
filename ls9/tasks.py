import math
# def sum_list(list1, list2):

#     length = min([len(list1), len(list2)])
#     max_length = max([len(list1), len(list2)])
#     numbers = list()
#     for i in range(max_length):

#         if i < length:
#             numbers.append(list1[i])
#             numbers.append(list2[i])
#         elif i >= length:
#             if len(list1) > i:
#                 numbers.append(list1[i])
#             else:
#                 numbers.append(list2[i])

#     return numbers


# print(sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#       [11, 22, 33, 44, 55, 66, 77, 88]))

# У вас есть массив чисел, составьте из них максимальное число. Например:
def max_value(numbers):
    alt = dict()

    for number in numbers:
        alt.setdefault(int(str(number)[0]), number)

    basis = list(alt.keys())
    basis.sort()
    basis.reverse()
    number = ""
    for num in basis:
        number += str(alt[num])

    return number


print(max_value([923, 23, 54323, 11114]))
