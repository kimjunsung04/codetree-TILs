n = int(input())

cnt = 0
# cnt 안쓰고 짜보려다가 불필요하게 시간 너무보냄
for i in range(1, n+1):
    for j in range(1, n+1):
        if i % 2 == 0: cnt += 2
        else: cnt += 1
        print(cnt, end=" ")
    print()