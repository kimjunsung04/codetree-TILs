sum_val = 0
sum_num = 0
for _ in range(10):
    t = int(input())
    if t >= 0 and t <= 200:
        sum_val += t
        sum_num += 1
print(f"{sum_val} {sum_val/sum_num:.1f}")