y = int(input())

# Please write your code here.
def is_yn(n):
    if n % 100 == 0 and n % 400 != 0:
        return "false"
    if n % 4 == 0:
        return "true"
    return "false"

print(is_yn(y))