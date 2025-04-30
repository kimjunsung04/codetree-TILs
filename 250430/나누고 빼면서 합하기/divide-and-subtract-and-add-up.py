n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
def np():
    global n, m, A
    sum_val = 0
    while True:
        sum_val += A[m-1]
        if m <= 1:
            break
        if m % 2 != 0:
            m -= 1
        else:
            m //= 2
    return sum_val

print(np())