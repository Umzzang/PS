import sys

input = sys.stdin.readline

n = int(input())

<<<<<<< HEAD
stack = []

for _ in range(n):
    lst = list(map(int, input().split()))
    if lst[0] == 1:
        stack.append(lst[1])
    elif lst[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif lst[0] == 3:
        print(len(stack))
    elif lst[0] == 4:
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])    
        else:
            print(-1)
=======
lst = list(map(int, input().split()))

sort_lst = sorted(list(set(lst)))
# print(sort_lst)

dic = {}
for i in range(len(sort_lst)):
    dic[sort_lst[i]] = i
print(dic)
for i in range(n):
    print(dic[lst[i]], end=' ')
>>>>>>> c16723eeeea1671384cfe3cd4ee52df7ef4e7545
