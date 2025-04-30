M, D = map(int, input().split())

# Please write your code here.
def last_day_number(m):
    if m == 2:
        return 28
    if m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    
    return 31

def check_md(m, d):
    if m <= 12 and d <= last_day_number(m):
        return "Yes"
    
    return "No"

print(check_md(M, D))