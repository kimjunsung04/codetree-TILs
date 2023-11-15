a = input()
b = input()
for _ in range(len(a)//2):
    a = a.replace(b, "")
print(a)