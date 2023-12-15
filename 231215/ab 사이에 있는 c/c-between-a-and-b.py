a, b, c = map(int, input().split())
hm = False
for i in range(a, b + 1):
    if i % c == 0:
        hm = True
        break

if hm:
    print("YES")
else:
    print("NO")