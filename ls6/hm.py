N = input("Type N: ")

try:
    N = int(N)
except ValueError:
    print("Error N isn't number")
    exit()

if N == 0:
    print("Result 0")
    exit()

if N < 1:
    print("Error N under 0")
    exit()

calculated_sum = 0

for i in range(1, N+1):
    calculated_sum += 1 / i

print(f'Result {"{:.2f}".format(calculated_sum)}')
