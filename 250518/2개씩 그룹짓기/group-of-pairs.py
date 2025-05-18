n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()

max_sum = 0
for i in range(n):
    group = nums[i] + nums[2*n - 1 - i]
    if group > max_sum:
        max_sum = group

print(max_sum)