n_list = [list(map(int, input().split())) for _ in range(3)]
input()
n_list2 = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        print(n_list[i][j]*n_list2[i][j], end=" ")
    print()