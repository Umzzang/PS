import sys

input = sys.stdin.readline

n = int(input())

score = list(map(int, input().split()))
score.sort()

answer = 0
print(score)
for i in range(n-2):
    first = score[i]
    target = 0 - first

    l = i+1
    r = l+1
    while l<=r:
        print(i, target, l, r)
        s = score[l] + score[r]
        if target == s:
            answer += 1
            l += 1
        elif target < s:
            l += 1
        else:
            r+=1
        if r>n-1:
            break

print(answer)

