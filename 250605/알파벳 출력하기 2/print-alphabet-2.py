n = int(input())

cnt = "A"

for i in range(n, 0, -1):
    for j in range(n-i):
        print("  ", end="")
    for j in range(i):
        print(cnt, end=" ")
        cnt = "A" if cnt == "Z" else chr(ord(cnt)+1)
    print()