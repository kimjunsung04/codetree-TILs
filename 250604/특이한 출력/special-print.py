n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        print((i, j), end=" ")
        if (i+j) % 4 == 0:
            print()
            