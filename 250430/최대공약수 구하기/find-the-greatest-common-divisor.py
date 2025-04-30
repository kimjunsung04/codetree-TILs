n, m = map(int, input().split())

# Please write your code here.
def gcd(n, m):
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            print(i)
            break
gcd(n, m)