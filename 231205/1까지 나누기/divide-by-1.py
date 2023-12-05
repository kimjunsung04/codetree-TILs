n = int(input())
for i in range(1, 10000):
    n /= i
    if n < 1:
        print(i)
        break