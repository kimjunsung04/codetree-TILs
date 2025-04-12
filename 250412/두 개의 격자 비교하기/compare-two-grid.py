n, m = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]
n_list2 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if n_list[i][j] == n_list2[i][j]:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()