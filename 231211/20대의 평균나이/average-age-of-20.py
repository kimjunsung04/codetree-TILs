sum_val = 0
num_val = 0
while True:
    t = int(input())
    if str(t)[0] != "2":
        break
    sum_val += t
    num_val += 1
print(f"{sum_val/num_val:.2f}")