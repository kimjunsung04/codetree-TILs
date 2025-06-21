n_list = list(map(int, input().split()))

count_list = [0] * 10

for i in n_list:
    if i < 10: break
    if i == 100:
        count_list[-1] += 1
    else:
        count_list[int(str(i)[0])-1] += 1

for i in range(10, 0, -1):
    print(f"{10*i} - {count_list[i-1]}")