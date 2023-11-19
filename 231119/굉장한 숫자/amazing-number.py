n = int(input())
print("true" if (n % 2 != 0 and n % 3 == 0) or (n % 2 == 0 and n % 5 == 0) else "false")