n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        if i % 2 == 0:
            print(n*i-j+1, end=" ")
        else:
            print(n*(i-1)+j, end=" ")
    print()