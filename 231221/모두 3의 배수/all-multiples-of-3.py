result = 1 
for _ in range(5):
    num = int(input())
    if num % 3 != 0:
        result = 0
print(result)