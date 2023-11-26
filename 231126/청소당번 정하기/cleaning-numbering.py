n = int(input())
c=b=h=0
for i in range(0, n+1):
    if i == 0: continue
    if i % 12 == 0:
        h += 1
    elif i % 3 == 0:
        b += 1
    elif i % 2 == 0:
        c += 1
print(c, b, h)