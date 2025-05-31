nums = list(map(int, input().split()))

for i in range(len(nums)):
    if nums[i] >= 250:
        nums = nums[:i]
        break

print(sum(nums), sum(nums)/len(nums))