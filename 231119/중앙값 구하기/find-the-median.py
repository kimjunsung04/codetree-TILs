a, b, c = map(int, input().split())
if b >= a >= c or c >= a >= b:
    print(a)
if a >= b >= c or c >= b >= a:
    print(b)
if a >= c >= b or b >= c >= a:
    print(c)