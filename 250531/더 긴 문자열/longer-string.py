a, b = map(str, input().split())
if len(a) > len(b):
    print(a, len(a))
elif len(b) > len(a):
    print(b, len(b))
else:
    print("same")