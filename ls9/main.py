def k_search(numbers=None, k=None):
    if not (numbers and k):
        return "Error: missing 1 required positional argumnet k"

    if type(numbers) != list:
        return "Error: argument numbers isn't list type"

    if type(k) != int:
        return "Error: argument k isn't list type"

    basis = set()
    for number in numbers:
        search = k - number
        if search in basis:
            return (search, number)
        basis.add(number)


a = k_search([1, 2, 3, 4, 5], 5)
b = k_search([1, 2, 3, 4, 5], 6)
c = k_search([1, 2, 3, 4, 5], 7)
d = k_search([1, 2, 3])
e = k_search("asddasdasd", 1)
f = k_search([1, 2, 3], "asdfsdf")
print(a, b, c, d, e, f)
