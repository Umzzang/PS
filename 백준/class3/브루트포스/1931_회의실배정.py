import sys
input = sys.stdin.readline
n = int(input())
time = []
for _ in range(n):
    s, e = map(int, input().split())
    time.append((s, e))

time.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end = time[0][1]
for i in range(1, len(time)):
    if end <= time[i][0]:
        cnt += 1
        end = time[i][1]

print(cnt)


# 끝나는 시간 순으로 정렬하면 앞에가 무조건 먼저끝나기 때문에 상관없음