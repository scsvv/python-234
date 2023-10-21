# Пользователь вводит число N. Найдите сумму чисел: 1 + 1.1 + 1.2 + 1.3 + ... + (1 + N / 10).

N = input("Type N: ")

try:
    N = int(N)
except ValueError:
    print("Fatal Error: Non-Valid data type")
    exit()

if N <= 0:
    print("Fatal Error: Non-Valid Value interval")
    exit()

_sum = 0
for i in range(0, N+1):
    data = 1 + i/10
    _sum = _sum + data
    print(data)

print(_sum)
