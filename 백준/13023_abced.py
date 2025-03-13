import sys

input = sys.stdin.readline
n,m = map(int,input().split())
friends = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)
# def abcde(i:list,j):
#     # print(i, j)
#     if j not in i:
#         copyi = i[:]
#         copyi.append(j)
#         if len(i) == 5:
#             # print(i)
#             return 1
#         for friend in friends[j]:
#             r = abcde(copyi, friend)
#             if r == 1:
#                 return r
#             else:
#                 continue
        
#     return 0


# result = 0
# for i in range(n):
#     for friend in friends[i]:
#         result =  abcde([i], friend)
#         if result:
#             break
#     if result:
#         break
# # print(friends)
# print(result)

# print(friends)  # index 가 사람번호 value가 index의 친구들
answer = 0
for i in range(n):  # 모든 사람 순회
    visited = [0] * (n+1)
    stack = [([i], 1)]
    while stack:
        x, l = stack.pop()
        if l ==5:
            answer = 1
            break
        
        for friend in friends[x[-1]]:
            if friend not in x:
                stack.append((x +[friend], l+1))
                
    if answer == 1:
        break
print(answer)

