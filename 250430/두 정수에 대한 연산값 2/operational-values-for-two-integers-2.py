a, b = map(int, input().split())

# Please write your code here.
def ab_math(a, b):
    a_r = a*2 if a > b else a+10
    b_r = b*2 if b > a else b+10
    return a_r, b_r
    

print(*ab_math(a, b))