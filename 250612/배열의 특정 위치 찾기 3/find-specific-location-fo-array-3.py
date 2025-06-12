n_list = list(map(int, input().split()))

zero_point = n_list.index(0)
sum_val = 0
for i in range(zero_point-3, zero_point):
    sum_val += n_list[i]
print(sum_val)