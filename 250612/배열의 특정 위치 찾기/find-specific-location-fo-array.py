n_list = list(map(int, input().split()))

sum_val = 0
cnt = 0
for i in range(len(n_list)):
    if i % 2 != 0 or i+1 % 3 == 0:
        sum_val += n_list[i]
        cnt += 1

print(f"{sum_val} {sum_val/cnt:.01f}")