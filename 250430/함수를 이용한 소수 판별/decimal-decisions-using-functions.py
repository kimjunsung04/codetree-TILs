a, b = map(int, input().split())

# Please write your code here.
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def primes(a, b):
    sum_val = 0
    for i in range(a, b+1):
        if is_prime(i):
            sum_val+=i
    return sum_val

print(primes(a, b))