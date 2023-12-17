a, b = map(int, input().split())
for i in range(1, 1000):
    if 1920%i == 0 and 2880%i == 0:
        if a <= i <= b:
            print(1)
            break
else:
    print(0)