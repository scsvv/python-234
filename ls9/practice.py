# def circle(r=None):
#     if not (r):
#         return "Invalid data"

#     if type(r) != int or type(r) != float:
#         try:
#             r = int(r)
#         except ValueError:
#             return "Invalid data"

#     return 3.14 * r ** 2


# print(circle(1))
# print(circle(2))
# print(circle(3))
# print(circle("3"))
# print(circle(" 4 "))
# print(circle("dfv"))

def even_counter(numbers: list = None) -> int:
    """even counter ele in list 

    Args:
        numbers (list, optional): _description_. Defaults to [].

    Returns:
        int: _description_
    """
    if numbers is None:
        return 0

    counter = 0
    for number in numbers:
        if number % 2 == 0:
            counter += 1
    return counter


print(even_counter([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(even_counter([2, 2, 2, 4, 2, 6, 2, 8, 2]))
