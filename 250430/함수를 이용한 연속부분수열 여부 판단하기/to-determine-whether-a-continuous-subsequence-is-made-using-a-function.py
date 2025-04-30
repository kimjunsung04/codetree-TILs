n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.

def check_sy(a, b):
    a_str = f",{','.join(list(map(str, a)))},"
    b_str = f",{','.join(list(map(str, b)))},"
    return "Yes" if b_str in a_str else "No"

print(check_sy(a, b))