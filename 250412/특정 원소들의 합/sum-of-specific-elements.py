n_list = [list(map(int, input().split())) for i in range(4)]
sum_val = 0
for i in range(4):
    for j in range(0, i+1):
        sum_val += n_list[i][j]
print(sum_val)