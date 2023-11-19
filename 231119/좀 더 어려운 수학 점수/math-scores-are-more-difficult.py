s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())
if (s1 != s2 and s1 > s2) or (s1 == s2 and e1 > e2):
    print("A")
else:
    print("B")