import sys

input = sys.stdin.readline

def main():
    tc = int(input())
    for _ in range(tc):
        k = int(input())
        chapter = list(map(int, input().split()))
        s_chapter = [0] * k
        s_chapter[0] = chapter[0]
        for i in range(1,k):
            s_chapter[i] = chapter[i] + s_chapter[i-1]

        dp = [[0] * (k) for _ in range(k)]      #dp[i][j] 는 i에서 j까지의 합
        for i in range(k-1):
            for j in range(i+1, i+2):
                dp[i][j] = s_chapter[j] - s_chapter[i] + chapter[i]

        for i in range(2, k):
            for j in range(k-2):
                dp[j][i] = min(dp[j][i-1], dp[j+1][i]) + chapter[i]




        print(dp[0][k-1])

if __name__ == "__main__":
    main()