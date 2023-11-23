a, b = map(int, input().split())
for _ in range(a, b):
    if a > b: break
    print(a, end=" ")
    if a % 2 != 0:
        a *= 2
    else:
        a += 3