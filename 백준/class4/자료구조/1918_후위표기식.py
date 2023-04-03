# 왜케 어렵지;

cal = list(input())
stack = []
ans = ''
for s in cal:
    if s.isalpha():
        ans += s
    elif s == '(':
        stack.append(s)
    elif s == ')':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.pop()
    elif s == '*' or s == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            ans += stack.pop()
        stack.append(s)
    elif s == '+' or s == '-':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.append(s)

while stack:
    ans += stack.pop()

print(ans)





