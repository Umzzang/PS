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
        if lst[i] > lst[i-1]:
            if lst[i] > max:
                answer += '+' * (lst[i] - max) + '-'
                max = lst[i]
            else:
                answer = 'NO'
        else:
            answer += '-' 
    

print(*answer, sep='\n')