import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())

score = list(map(int, input().split()))
score.sort()

# cnt = {}
# for sc in score:
#     if cnt.get(sc):
#         cnt[sc] += 1
#     else:
#         cnt[sc] = 1

answer = 0
# print(score)
for i in range(n-2):
    first = score[i]
    target = 0 - first

    l = i+1
    r = n-1
    while l<r:
        now = score[l] + score[r]
        # print(target, l, r)
        if target == now:
            if score[l] == score[r]:
                answer += (r-l)
                l += 1
            else:
                rcnt = 0
                lcnt = 0
                before = score[l]
                while now == score[l] + score[r]:
                    rcnt += 1
                    r -= 1
                while score[l] == before:
                    lcnt += 1
                    l += 1
                answer += lcnt * rcnt
                # answer += cnt[score[l]] * cnt[score[r]]
                # l += cnt[score[l]]
                # r -= cnt[score[r]]
                # idx = bisect_left(score, score[r])
                # answer += r-idx + 1
                # l += 1


        elif target > now:
            l += 1
        else:
            r -= 1

print(answer)

