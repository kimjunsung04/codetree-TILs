a, b = map(int, input().split())

# Please write your code here.
def num_check(i):
    return (
        "3" in str(i) or
        "6" in str(i) or
        "9" in str(i)
    ) or i % 3 == 0

def game(a, b):
    sum_num = 0
    for i in range(a, b+1):
        if num_check(i):
            sum_num += 1
    return sum_num

print(game(a, b))