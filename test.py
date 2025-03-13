import sys

input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

sort_lst = sorted(list(set(lst)))
# print(sort_lst)

dic = {}
for i in range(len(sort_lst)):
    dic[sort_lst[i]] = i
print(dic)
for i in range(n):
    print(dic[lst[i]], end=' ')