n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def absolute_arr(copy_arr):
    return [abs(i) for i in copy_arr]

result = absolute_arr(arr[:])
print(*result)