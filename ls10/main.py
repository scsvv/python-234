import math


def from_integer_to_roman(argument: int):
    """_summary_

    Args:
        number (int): _description_

    Returns:
        _type_: _description_
    """
    if argument == 0:
        return ""
    if argument > 4000:
        return "ERROR"

    voc = {
        0: ["I", "IV", "V", "IX"],
        1: ["X", "XL", "L", "XC"],
        2: ["C", "CD", "D", "CM"],
        3: ["M", "Mv", "v", "MX̅"]
    }

    decimal = math.floor(math.log10(argument))
    number = argument // 10 ** decimal
    less = argument % 10 ** decimal
    if number < 4:
        return f"{voc[decimal][0] * number}{from_integer_to_roman(less)}"
    elif number == 4:
        return f"{voc[decimal][1]}{from_integer_to_roman(less)}"
    elif number == 5:
        return f"{voc[decimal][2]}{from_integer_to_roman(less)}"
    elif number > 5:
        return f"{voc[decimal][2]}{voc[decimal][0]*(number - 5)}{from_integer_to_roman(less)}"
    elif number == 9:
        return f"{voc[decimal][3]}{from_integer_to_roman(less)}"


print(from_integer_to_roman(3600))


# 1_000_000 -> 1M 23_000 -> 23K
# def number_str_gen(number):
#     dec = math.log10(number)
#     result = round(number / (10 ** (dec - dec % 3)), 2)
#     if dec >= 3 and dec < 6:

#         print(f'{result}K')
#     elif dec >= 6 and dec < 9:
#         print(f'{result}M')
#     elif dec >= 9 and dec < 12:
#         print(f'{result}B')


# number_str_gen(1234)
# number_str_gen(12345)
# number_str_gen(123456)
# number_str_gen(1234567)
# number_str_gen(12345678)
# number_str_gen(123456789)
# number_str_gen(1234567123)
