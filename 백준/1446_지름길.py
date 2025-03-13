import sys
import heapq
input = sys.stdin.readline

n, d = map(int, input().split())
cuts = []
length = [i for i in range(10001)]
for _ in range(n):
    # start, end, dd = map(int, input().split())
    cuts.append(list(map(int, input().split())))

cuts.sort(key=lambda x : x[1])

for cut in cuts:
    start, end, dd = cut
    if length[end] > length[start] + dd:
        length[end] = length[start] + dd
        for j in range(end+1, 10001):
            length[j] = length[j-1] + 1

print(length[d])