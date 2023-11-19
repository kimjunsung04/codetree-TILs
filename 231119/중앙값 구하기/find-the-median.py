a, b, c = map(int, input().split())
if (b >= a and a >= c) or (c >= a and a >= a):
    print(a)
elif (a >= b and b >= c) or (c >= b and b >= a):
    print(b)
elif (a >= c and c >= b) or (b >= c and c >= a):
    print(a)