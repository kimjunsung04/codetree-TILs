a, b, c = map(int, input().split())

if a > b and c > a:
    print(a)
elif b > a and c > b:
    print(b)
else:
    print(c)