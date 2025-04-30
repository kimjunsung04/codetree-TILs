n = int(input())

# Please write your code here.
def even_and_5bs(n):
    n1, n2 = map(int, list(str(n)))
    return "Yes" if n % 2 == 0 and (n1+n2) % 5 == 0 else "No"

print(even_and_5bs(n))