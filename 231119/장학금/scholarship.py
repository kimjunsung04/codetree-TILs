a, b = map(int, input().split())
if a >= 90:
    if b >= 95:
        print(10)
    elif b >= 90:
        print(5)
else:
    print(0)