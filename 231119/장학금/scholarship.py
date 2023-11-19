a, b = map(int, input().split())
if a >= 90:
    if b >= 95:
        print(100000)
    elif b >= 90:
        print(50000)
    else:
        print(0)
else:
    print(0)