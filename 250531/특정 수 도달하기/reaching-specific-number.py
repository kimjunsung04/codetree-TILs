nums = list(map(int, input().split()))

sum_val = 0
cnt = 0
for num in nums:
    if num >= 250:
        break
    sum_val += num
    cnt += 1

print(sum_val, round(sum_val/cnt, 1))