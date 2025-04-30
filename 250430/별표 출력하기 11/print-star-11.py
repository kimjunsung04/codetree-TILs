n = int(input())

size = 2 * n + 1
for i in range(size):
    for j in range(size):
        if i % 2 == 0 or j % 2 == 0:
            print("* ", end="")
        else:
            print("  ", end="")
    print()