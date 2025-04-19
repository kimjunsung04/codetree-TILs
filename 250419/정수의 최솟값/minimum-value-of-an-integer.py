a, b, c = map(int, input().split())

# Please write your code here.
def get_min(a,b,c):
    min_val = a
    if min_val > b:
        min_val = b
    if min_val > c:
        min_val = c

    print(min_val)


get_min(a, b, c)