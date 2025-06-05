start, end = map(int, input().split())

ys_three_cnt = 0
# Please write your code here.
for i in range(start, end+1):
    ys_cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            ys_cnt += 1
    if ys_cnt == 3: ys_three_cnt += 1
print(ys_three_cnt)