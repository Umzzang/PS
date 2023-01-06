m, n = map(int,input().split(' '))
answer = [0] * (n+1)
a = []
for i in range(2, n+1):
    if answer[i] == 0:
        a.append(i)
        k = 1
        
        while k*i <= n:
            answer[k*i] = 1
            k += 1


for i in a:
    if m <= i <= n:
        print(i)

