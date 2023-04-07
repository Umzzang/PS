s = input()
bs = list(input())

lastword = bs[-1]
bs_len = len(bs)

stack = []
for a in s:
    stack.append(a)
    if a == lastword:
        if stack[-1 * bs_len:] == bs:
            del stack[-1 * bs_len:]
if stack:
    print("".join(stack))
else:
    print('FRULA')