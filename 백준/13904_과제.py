import sys
import heapq
input = sys.stdin.readline

n = int(input())
score = 0
day = 0
ds = []
dss = {}
for _ in range(n):
    d, s = map(int, input().split())
    day = max(d, day)
    # heapq.heappush(ds, (-d, s))
    if dss.get(d):
        dss[d].append(s)
    else:
        dss[d] = [s]

dayscore = []

# for i in sorted(list(dss.keys()), reverse=True):
#     for d in dss[i]:
#         # print(i, d)
#         heapq.heappush(dayscore, -d)
#     s = heapq.heappop(dayscore)
#     print(s)
#     score -= s

for i in range(day, 0, -1):
    # print(i)
    if dss.get(i):
        for d in dss[i]:
            heapq.heappush(dayscore, -d)
    if dayscore:
        s = heapq.heappop(dayscore)
        # print(s)
        score -= s


# while day>0:
#     if ds:
#         d, s = heapq.heappop(ds)
#     print(d,s)
#     if day == -d:
#         heapq.heappush(dayscore, -s)
#     else:
#         score -= heapq.heappop(dayscore)
#         print(score)
#         heapq.heappush(dayscore, -s)
#         day = -d



print(score)



