n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_of_list(arr, idx):
    if idx == len(arr) - 1:
        return arr[idx]
    return lcm(arr[idx], lcm_of_list(arr, idx + 1))

print(lcm_of_list(arr, 0))