n_list = list(map(int, input().split()))

last = 0
sum_val = 0
for i in range(len(n_list)):
    if n_list[i] == 0:
        break
    last += 1
    sum_val += n_list[i]
print(f"{sum_val} {sum_val/last:.1f}")