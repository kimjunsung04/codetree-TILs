a, b = map(int, input().split())

# Please write your code here.
def ab_math(a, b):
    a_r = a+25 if a > b else a*2
    b_r = b+25 if b > a else b*2
    return a_r, b_r
    

print(*ab_math(a, b))