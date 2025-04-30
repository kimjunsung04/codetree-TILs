n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def index_sum(a, b):
    return sum(arr[a:b])

def index_sums():
    for item in queries:
        print(index_sum(item[0]-1, item[1]))

index_sums()