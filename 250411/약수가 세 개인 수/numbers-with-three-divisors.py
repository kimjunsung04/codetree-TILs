start, end = map(int, input().split())
ys_num = 0

# Please write your code here.
for i in range(start, end+1):
    temp_yc = 0
    for j in range(1, i+1):
        if i % j == 0:
            temp_yc += 1
    if temp_yc == 3: ys_num += 1
print(ys_num)