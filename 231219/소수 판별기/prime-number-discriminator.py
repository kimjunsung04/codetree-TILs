n = int(input())
if n < 2:
    result = 'C'
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    result = 'P' if is_prime else 'C'
print(result)