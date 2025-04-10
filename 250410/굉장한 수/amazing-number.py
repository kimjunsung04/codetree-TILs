n = int(input())
if n % 2 != 0 and n % 3 == 0 or n % 2 == 0 and n % 5 == 0:
    print("true")
else:
    print("false")