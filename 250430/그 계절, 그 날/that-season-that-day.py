Y, M, D = map(int, input().split())

# Please write your code here.
def check_yn(y):
    if y % 4 == 0 and y % 100 == 0 and y % 400 == 0: return True
    elif y % 4 == 0 and y % 100 == 0: return False
    elif y % 4 == 0: return True
    return False

def last_day_number(y, m):
    if m == 2 and check_yn(y):
        return 29
    elif m == 2:
        return 28
    if m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    
    return 31

def check_ymd(y, m, d):
    if m > 12 or m < 1:
        return False
    last_day = last_day_number(y, m)
    if d > last_day or d < 1:
        return False
    return True

def check_season(m):
    if m in [3,4,5]:
        return "Spring"
    elif m in [6,7,8]:
        return "Summer"
    elif m in [9,10,11]:
        return "Fall"
    elif m in [12,1,2]:
        return "Winter"

if not check_ymd(Y, M, D):
    print(-1)
else:
    print(check_season(M))