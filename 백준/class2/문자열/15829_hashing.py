import sys
input = sys.stdin.readline

l = int(input())
aa = list(input().rstrip())
ans = 0
for i in range(len(aa)):
    ans += (ord(aa[i]) - 96) * (31 ** i)
print(ans%1234567891)