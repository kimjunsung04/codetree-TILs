a, b = map(int, input().split())

# Please write your code here.
def check_sosu(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def check_num_split_sum(n):
    n_list = list(map(int, list(str(n))))
    return sum(n_list) % 2 == 0

def hap_sosu_check(a, b):
    count = 0
    for i in range(a, b+1):
        if check_num_split_sum(i) and check_sosu(i):
            count += 1
    return count

print(hap_sosu_check(a, b))