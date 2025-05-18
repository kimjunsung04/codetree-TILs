n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
arr = []
res = []

for i, j in enumerate(nums, 1):
    arr.append(j)
    if i % 2 == 1:
        arr.sort()
        res.append(arr[len(arr)//2])

print(*res)