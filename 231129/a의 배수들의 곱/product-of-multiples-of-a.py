a, b = map(int, input().split())
prod = 1
for i in range(1, b+1):
    if i % a == 0:
        prod *= i
print(prod)