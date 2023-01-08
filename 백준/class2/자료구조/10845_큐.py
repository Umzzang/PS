import sys

n = int(sys.stdin.readline())
q = []
for i in range(n):
    o = sys.stdin.readline()
    if o[:3] == 'pus':
        a, b = o.split(' ')
        q.append(int(b))
    elif o[:3] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop(0))
    elif o[:3] == 'siz':
        print(len(q))
    elif o[:3] == 'emp':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif o[:3] == 'fro':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif o[:3] == 'bac':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])