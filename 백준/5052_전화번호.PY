import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dict = {}
    answer = 'YES'
    calls = []
    for _ in range(n):
        call = input().rstrip()
        calls.append(call)
        now = ''
        for i in range(len(call)):
            now += call[i]
            if dict.get(now):
                answer = 'NO'
                break
        else:
            dict[call] = 1
    for call in calls:
        now = ''
        for i in range(len(call)-1):
            now += call[i]
            if dict.get(now):
                answer = 'NO'
                break
        if answer == 'NO':
            break
    print(answer)