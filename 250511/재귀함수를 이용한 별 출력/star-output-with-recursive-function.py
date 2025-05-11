n = int(input())

# Please write your code here.
def star(x, y):
    for i in range(x):
        print("*", end="")
    print()
    if x >= y: return
    star(x+1, y)

star(1, n)