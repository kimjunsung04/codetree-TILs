s = input().split()
if len(s[0]) > len(s[1]):
    print(s[0], len(s[0]))
elif len(s[1]) > len(s[0]):
    print(s[1], len(s[1]))
else:
    print("same")