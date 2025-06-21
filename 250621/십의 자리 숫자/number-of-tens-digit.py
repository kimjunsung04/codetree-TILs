n_list = list(map(int, input().split()))

count_list = [0] * 9

for i in n_list:
    if i == 0: break
    if i > 9:
        count_list[int(str(i)[0])-1] += 1


for i in range(len(count_list)):
    print(f"{i+1} - {count_list[i]}")