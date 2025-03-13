import sys
input = sys.stdin.readline

n = int(input())
lst = []
answer = []

max = 1
for i in range(n):
    num = int(input())
    while max <= num:
        lst.append(max)
        answer.append('+')
        max += 1
    if lst[-1] == num:
        lst.pop()
        answer.append('-')
    else:
        answer = 'NO'
        break

if answer == 'NO':
    print(answer)
else:
    for i in answer:
        print(i)

# input 말고 무조건 sys.stdin.readline으로 시간 많이 단축
# 문자열로 더해서 나누는 것보다 배열에 append한후에 for문 돌리는 것이 더 짧다. => 이유찾자


# 작다고 무조건 pop이 되는것이 아니라서 틀림
# for i in range(n):
#     lst.append(int(input()))
# max = 0
# for i in range(len(lst)):
#     if i == 0:
#         max = lst[i]
#         answer += '+' * lst[i] + '-'
#     else:
#         if lst[i] > lst[i-1]:
#             if lst[i] > max:
#                 answer += '+' * (lst[i] - max) + '-'
#                 max = lst[i]
#             else:
#                 answer = 'NO'
#                 break
#         else:
#             answer += '-' 
    
# if answer == 'NO':
#     print(answer)
# else:
#     print(*answer, sep='\n')

