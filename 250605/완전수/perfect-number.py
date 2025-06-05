start, end = map(int, input().split())

wan_cnt = 0
# Please write your code here.
for i in range(start, end+1):
    jin_sum = 0
    for j in range(1, i+1):
        if i % j == 0 and j != i:
            jin_sum += j
    if i == jin_sum:
        wan_cnt += 1
print(wan_cnt)