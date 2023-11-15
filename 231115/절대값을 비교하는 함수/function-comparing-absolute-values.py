for _ in range(int(input())):
    a, b = map(int, input().split())
    if a < 0: a = -a
    if b < 0: b = -b
    print(max(a, b))