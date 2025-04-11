n_list = [int(input()) for _ in range(10)]
e3_num = 0
e5_num = 0
for item in n_list:
    if item % 3 == 0:
        e3_num += 1
    if item % 5 == 0:
        e5_num += 1
print(e3_num, e5_num)