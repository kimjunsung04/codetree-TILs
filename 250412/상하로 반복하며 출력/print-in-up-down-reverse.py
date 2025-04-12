n = int(input())
for i in range(1, n+1):
    for j in range(1, n+1):
        if j % 2 != 0:
            print(i, end="")
        else:
            print(n-i+1, end="")
    print()
