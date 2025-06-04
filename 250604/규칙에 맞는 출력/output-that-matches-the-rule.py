n = int(input())

for i in range(n):
    for j in range(i+1, 0, -1):
        print(j, end=" ")
    print()