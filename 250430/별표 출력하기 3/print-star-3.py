n = int(input())

for i in range(n):
    for j in range(i):
        print("  ", end="")
    for j in range(n, i, -1):
        print("* ", end="")
    for j in range(n-1, i, -1):
        print("* ", end="")
    print()