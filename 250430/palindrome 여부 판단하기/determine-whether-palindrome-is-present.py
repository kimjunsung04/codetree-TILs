A = input()

# Please write your code here.
def check_palindrome(a):
    return a[::-1] == a

print("Yes" if check_palindrome(A) else "No")