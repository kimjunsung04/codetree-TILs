n = int(input())

for i in range(n-1, 0, -1):
    for j in range(n-i):
        print("*", end="")
    print("\n")

for i in range(n):
    for j in range(n-i):
        print("*", end="")
    print("\n")
