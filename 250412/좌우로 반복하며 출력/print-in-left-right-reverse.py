n = int(input())
for i in range(n):
    row = []
    for j in range(1, n+1):
        row.append(j)
    if i % 2 != 0:
        row.reverse()
    for item in row:
        print(item, end="")