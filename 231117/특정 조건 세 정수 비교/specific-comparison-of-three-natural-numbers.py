a, b, c = map(int, input().split())
print(f"{1 if a == min([a, b, c]) else 0} {1 if len(set([a,b,c]))==1 else 0}")