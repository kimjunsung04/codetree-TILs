a, b = map(int, input().split())
remainder = a % b
result = str(a // b) + "."
for _ in range(20):
    remainder *= 10
    quotient = remainder // b
    result += str(quotient)
    remainder %= b
print(result)