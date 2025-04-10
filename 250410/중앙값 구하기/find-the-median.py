a, b, c = map(int, input().split())

if a > b and c > a or a > c and b > a:
    print(a)
elif b > a and c > b or b > c and a > b:
    print(b)
else:
    print(c)