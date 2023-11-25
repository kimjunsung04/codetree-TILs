n3 = 0
n5 = 0
for _ in range(10):
    i = int(input())
    if i % 3 == 0:
        n3 += 1
    if i % 5 == 0:
        n5 += 1
print(n3, n5)