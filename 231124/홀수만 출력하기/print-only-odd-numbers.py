n = int(input())
for _ in range(n):
    t = int(input())
    if t % 2 != 0 and t % 3 == 0:
        print(t)