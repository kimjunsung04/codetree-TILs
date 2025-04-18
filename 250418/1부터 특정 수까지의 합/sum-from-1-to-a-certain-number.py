n = int(input())

# Please write your code here.
def nsum(n):
    temp_sum = 0
    for i in range(1, n+1):
        temp_sum += i
    print(temp_sum//10)
nsum(n)