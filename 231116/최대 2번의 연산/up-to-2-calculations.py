a = int(input())
if a % 2 == 0:
    a //= 2
if a % 2 != 0:
    a = (a+1)//2
print(a)