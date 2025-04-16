n, m = map(int, input().split())

# Please write your code here.
def lcm(n, m):
    for i in range(max(n, m), max(n, m)*30):
        if i % n == 0 and i % m == 0:
            print(i)
            break
lcm(n, m)