n_list = [list(map(str, input().split())) for _ in range(3)]
count_list = [0]*4

for a, b in n_list:
    b = int(b)
    if a == "Y" and b >= 37:
        count_list[0] += 1
    elif a == "N" and b >= 37:
        count_list[1] += 1
    elif a == "Y":
        count_list[2] += 1
    else:
        count_list[3] += 1

for i in count_list:
    print(i, end=" ")
if count_list[0] >= 2: print("E")