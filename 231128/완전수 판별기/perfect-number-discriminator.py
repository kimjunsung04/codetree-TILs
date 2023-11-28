n = int(input()) 
sum_val = 0
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        sum_val += 1
print("N" if n == sum_val else "P")