a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def run_math(a, o, c):
    if o == "+": return a+c
    elif o == "-": return a-c
    elif o == "/": return int(a/c)
    elif o == "*": return a*c
    else: return False

result = run_math(a, o, c)
if result:
    print(f"{a} {o} {c} = {result}")
else:
    print(result)