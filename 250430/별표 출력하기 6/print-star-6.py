n = int(input())

for i in range(n):
    for j in range(i):
        print("  ", end="")
    for j in range(2 * (n - i) - 1):
        print("* ", end="")
    print()
for i in range(n - 2, -1, -1):
    for j in range(i):
        print("  ", end="")
    for j in range(2 * (n - i) - 1):
        print("* ", end="")
    print()
