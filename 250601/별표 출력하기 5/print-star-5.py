n = int(input())

for i in range(n, 0, -1):
    for _ in range(i, 0, -1):
        for _ in range(i, 0, -1):
            print("*", end="")
        print(" ", end="")
    print()