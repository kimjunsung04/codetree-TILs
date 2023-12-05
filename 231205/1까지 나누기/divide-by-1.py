n = int(input())
for i in range(1, 100):
    n //= i
    if n < 1:
        print(i)
        break