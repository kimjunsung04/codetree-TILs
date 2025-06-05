n = int(input())

cnt = 65

for i in range(n):
    for j in range(n):
        print(chr(cnt), end="")
        cnt += 1
    print()