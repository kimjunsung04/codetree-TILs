n = int(input()) 
sum_val = 0
for i in range(1, n):
    if i % n == 0:
        sum_val += 1
print("N" if n == sum_val else "P")