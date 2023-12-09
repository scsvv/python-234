def is_palindrome(x: int) -> bool:
    return int(str(x)[::-1]) == x


print(is_palindrome(1234))
print(is_palindrome(1221))
print(is_palindrome(5))
print(is_palindrome(1234554321))
