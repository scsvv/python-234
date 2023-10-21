K = input("Type K: ")
N = input("Type N: ")

# FOR I IN RANGE(0, 10, 1)
try:
    N = int(N)
    K = int(K)
except ValueError:
    print("Fatal error: exit with status -1")
    exit()

if N > K:
    step = 1
elif K > N:
    step = -1
elif K == N:
    print(f'{K}\nsum = {K}')
    exit()

sum = 0

for i in range(K, N+step, step):
    print(i)
    if i % 2 == 1:
        continue
    sum = sum + i

print(f'sum = {sum}')
