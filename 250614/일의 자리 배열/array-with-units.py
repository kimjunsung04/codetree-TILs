n_list = list(map(int, input().split()))

for i in range(10):
    temp_num = 0
    if i == 2:
        temp_num = n_list[0]+n_list[1]
    elif i > 2:
        temp_num = n_list[i-2] + n_list[i-1]
    else:
        print(n_list[i], end=" ")
        continue
    if len(str(temp_num)) >= 2:
        temp_num = int(str(temp_num)[-1])
    n_list.append(temp_num)
    print(n_list[i], end=" ")