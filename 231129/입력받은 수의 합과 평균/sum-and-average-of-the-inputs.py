n = int(input())
sum_val = 0
for _ in range(n):
    t = int(input())
    sum_val += t
print(f"{sum_val} {sum_val/n:.1f}")