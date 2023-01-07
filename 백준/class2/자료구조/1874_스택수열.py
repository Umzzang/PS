n = int(input())
lst = []
answer = ''
for i in range(n):
    lst.append(int(input()))

max = 0
for i in range(len(lst)):
    if i == 0:
        max = lst[i]
        answer += '+' * lst[i] + '-'
    else:
        if lst[i] > max:
            max = lst[i]
            answer += '+' * (lst[i]-max) + '-'
        else:
            if lst[i-1] < lst[i]:
                answer = 'NO'
                break
            else:
                answer += '-' * (max-lst[i])
    

print(answer)