import sys

input  = sys.stdin.readline

def dfs(i):
    arr[i] = -2
    for j in range(n):
        if arr[j] == i :
            dfs(j)



n = int(input())
arr = list(map(int, input().split())) # i 는 노드 번호 arr[i] 가 i의 부모 노드
e = int(input())

dfs(e)
cnt = 0
# print(arr)
for i in range(n):
    if arr[i] != -2 and i not in arr:
        cnt += 1


print(cnt)