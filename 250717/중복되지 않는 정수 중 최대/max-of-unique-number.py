n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
max_num = -1
for item in nums:
    if nums.count(item) == 1 and max_num < item:
        max_num = item

print(max_num)