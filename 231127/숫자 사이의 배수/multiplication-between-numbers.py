a, b = map(int, input().split())
sum_val = 0
sum_num = 0
for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        sum_val += i
        sum_num += 1
print(f"{sum_val} {sum_val/sum_num:0.1f}")