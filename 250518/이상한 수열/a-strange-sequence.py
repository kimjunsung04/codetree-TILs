N = int(input())

# Please write your code here.
def esn(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return esn(n//3) + esn(n-1)

print(esn(N))