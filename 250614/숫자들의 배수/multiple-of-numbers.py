n = int(input())

arr = [n]

cnt = 1 if n % 5 == 0 else 0

for i in range(1, 10):
    temp_num = arr[i-1]+n
    if temp_num % 5 == 0:
        cnt += 1
    if cnt > 2:
        break
    arr.append(temp_num)

for i in arr:
    print(i, end=" ")