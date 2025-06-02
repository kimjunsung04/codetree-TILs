n = int(input())

for i in range(n*n-2):
    for j in range(n*n-2):
        if i % 2 == 0 or j % 2 == 0:
            print("* ", end="")
        else:
            print("  ", end="")
    print()