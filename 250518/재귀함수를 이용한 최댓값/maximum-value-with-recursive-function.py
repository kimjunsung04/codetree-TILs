n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def find_max(arr, n):
    if n == 1:
        return arr[0]
    return max(arr[n - 1], find_max(arr, n - 1))

result = find_max(arr, n)
print(result)