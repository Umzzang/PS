from collections import deque

cal = list(input())

c = ['+', '-', '*', '/']

i = 0
while i < len(cal):
    if cal[i] == '*' or cal[i] == '/':
        cal.insert(i+2, ')')
        cal.insert(i-1, '(')
        i += 1
    i += 1
answer = ''




# def make(lst):
#     print(lst)
#     if lst[0] == '(' or lst[0] == ')':
#         return make(lst[1:])
#     if len(lst) == 0:
#         return
#     if len(lst) == 3:
#         ans = str(lst[0]) + str(lst[1] + str(lst[2]))
#         return ans

#     if lst[1] in c:
#         return str(lst[0])  + make(lst[2:]) + str(lst[1])
    
   
    
# ans = make(cal)

print(ans)



