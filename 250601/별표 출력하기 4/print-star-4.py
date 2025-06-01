n = int(input())

for i in range(n):
    for _ in range(n-i):
        print("* ", end="")
    print()

for i in range(n-2, -1, -1):
    for _ in range(n-i):
        print("* ", end="")
    print()