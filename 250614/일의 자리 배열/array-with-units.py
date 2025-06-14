p1, p2 = map(int, input().split())

arr = [p1, p2]

for i in range(2, 10):
    arr.append((arr[i-2]+arr[i-1])%10)

for i in arr:
    print(i, end=" ")