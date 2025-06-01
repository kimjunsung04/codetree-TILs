n = int(input())

for i in range(n, -1, -1):
    for j in range(n-i):
        print("* ", end="")
    print()

for i in range(n):
    for j in range(n-i):
        print("* ", end="")
    print()