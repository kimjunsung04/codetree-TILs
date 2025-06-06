n = int(input())
avg = sum(list(map(float, input().split())))/n

print(f"{avg:.1f}")
if avg > 4: print("Perfect")
elif avg > 3: print("Good")
else: print("Poor")