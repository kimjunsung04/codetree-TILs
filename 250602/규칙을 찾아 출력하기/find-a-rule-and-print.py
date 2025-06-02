n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or j == n:
            print("* ", end="")
        elif i >= 2 and i-1 >= j:
            print("* ", end="")
        else:
            print("  ", end="")
    print()