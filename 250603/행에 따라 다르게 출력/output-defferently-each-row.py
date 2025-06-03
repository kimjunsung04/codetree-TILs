n = int(input())

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i % 2 == 0: cnt += 2
        else: cnt += 1
        print(cnt, end=" ")
    print()