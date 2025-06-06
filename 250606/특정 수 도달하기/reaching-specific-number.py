n_list = list(map(int, input().split()))

sum_val = 0
cnt = 1
for i in range(len(n_list)):
    if n_list[i] > 250:
        cnt = i
        break
    sum_val += n_list[i]
print(f"{sum_val} {sum_val/cnt:.1f}")