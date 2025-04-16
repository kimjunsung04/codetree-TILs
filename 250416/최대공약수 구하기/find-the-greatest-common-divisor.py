n, m = map(int, input().split())

# Please write your code here.
def gcd(n, m):
    n_gcd = []
    m_gcd = []
    for i in range(1, n+1):
        if n % i == 0: n_gcd.append(i)
    for i in range(1, m+1):
        if m % i == 0: m_gcd.append(i)
    print(list(set(n_gcd)&set(m_gcd))[-1])
gcd(n, m)