n_list = [list(map(int, input().split())) for _ in range(4)]
print(sum([1 for i in n_list for j in i if j % 5 == 0]))