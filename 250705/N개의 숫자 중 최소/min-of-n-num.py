n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
now = a[0]

for item in a:
    if now > item:
        now = item

print(now, a.count(now))