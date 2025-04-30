a, b = map(int, input().split())

# Please write your code here.
def check_num(i):
    return True if not (i % 2 == 0) and not (str(i)[-1] == "5") and not (i % 3 == 0 and i % 9 != 0) else False

def check_nums(a, b):
    count = 0
    for i in range(a, b+1):
        if check_num(i): count+=1
    return count

print(check_nums(a, b))