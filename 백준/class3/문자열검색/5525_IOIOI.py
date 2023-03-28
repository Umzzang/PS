import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
s = input()

target = 'IO' * n + 'I'

i = 0

cnt = 0

# def search(i):
#     if target[0] != s[i]:
#         return False, 1
#     for k in range(2*n + 1):
#         if target[k] == s[i]:
#             i += 1
#         else:
#             return False, k
#     else:
#         return True, 0

# while i<m-(2*n +1)+1:
#     k, j = search(i)
#     # print(i, k, j)
#     if k:
#         cnt += 1
#         i += 2
#     else:
#         i += j 

# print(cnt)


ncnt = 0
while i < m-2:
    # print(i, ncnt)
    if s[i] == 'I':
        if s[i+1] == 'O':
            if s[i+2] == 'I':
                ncnt += 1
                i += 2
                if ncnt == n:
                    cnt += 1
                    ncnt -= 1
            else:
                i += 3
                ncnt = 0
        else:
            i += 1
            ncnt = 0
    else:
        i += 1
        ncnt = 0

print(cnt)
