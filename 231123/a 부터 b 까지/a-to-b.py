a, b = map(int, input().split())
for i in range(int(a), b):
    if i >= b: break
    print(i, end=" ")
    if i % 2 != 0:
        i *= 2
    else:
        i *= 3