n = int(input())
sum_val = 0
for _ in range(n):
    t = int(input())
    if t % 2 != 0 and t % 3 == 0:
        sum_val += t
print(sum_val)