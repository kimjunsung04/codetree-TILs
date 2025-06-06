n_list = list(map(int, input().split()))

sum_val = 0
cnt = 0
for i in n_list:
    if i == 0:
        break
    if i % 2 == 0:
        sum_val += i 
        cnt += 1
print(f"{cnt} {sum_val}")