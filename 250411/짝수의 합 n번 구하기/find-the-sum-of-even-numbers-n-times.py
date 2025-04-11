n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    even_sum = 0
    for i in range(a, b+1):
        if i % 2 == 0:
            even_sum += i
    print(even_sum)