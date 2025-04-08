import sys
import heapq
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    elif b > a:
        parent[b] = a


def main():
    global parent
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]
    cost = []
    total = 0
    for _ in range(m):
        # a,b,c= map(int,input().split())
        # heapq.heappush(cost, [c,a,b])
        cost.append(list(map(int,input().split())))
    cost.sort(key=lambda x : x[2])
    # while cost:
    #     c, a, b = heapq.heappop(cost)
    #     if find(a) == find(b):
    #         continue
    #     else:
    #         union(a,b)
    #         total += c
    #         last = c
    for a,b,c in cost:
        if find(a) == find(b):
            continue
        else:
            union(a,b)
            total += c
            last = c
    print(total - last)

if __name__ == "__main__":
    main()