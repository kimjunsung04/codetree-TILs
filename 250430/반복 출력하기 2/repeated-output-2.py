n = int(input())

# Please write your code here.
def hello(n):
    if n == 0:
        return
    hello(n-1)
    print("HelloWorld")

hello(n)