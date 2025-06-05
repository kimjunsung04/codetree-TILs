n = int(input())


cnt = "A"

for i in range(n):
    for j in range(i+1):
        print(cnt, end="")
        cnt = "A" if cnt == "Z" else chr(ord(cnt) + 1)
    print()