import sys


# print(score)
def find(l, r, target, score):
    answer = 0
    while l<r:
        now = score[l] + score[r]
        # print(target, l, r)
        if target == now:
            if score[l] == score[r]:
                answer += ((r-l+1) * (r-l))//2
                break
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
        elif target > now:
            l += 1
        else:
            r -= 1
    return answer

def main():
    input = sys.stdin.readline
    n = int(input())
    score = list(map(int, input().split()))
    score.sort()
    answer = 0
    for i in range(n-2):
        first = score[i]
        target = 0 - first

        l = i+1
        r = n-1
        answer += find(l, r, target, score)

    print(answer)

if __name__ == "__main__":
    main()

