n = int(input())
n_list = [1, n]

for i in range(1, 100):
    temp_num = n_list[i-1] + n_list[i]
    n_list.append(temp_num)
    if temp_num > 100: break

for i in n_list:
    print(i, end=" ")