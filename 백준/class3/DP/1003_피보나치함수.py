m = [0] * 41
m[0] = [1, 0]
m[1] = [0, 1]

def fibonacci(n):
    if m[n] != 0:
        return m[n]
    if m[n] == 0:
        m[n] = [fibonacci(n-1)[0] + fibonacci(n-2)[0], fibonacci(n-1)[1] + fibonacci(n-2)[1]]
        return [fibonacci(n-1)[0] + fibonacci(n-2)[0], fibonacci(n-1)[1] + fibonacci(n-2)[1]]
        

    

    


t = int(input())
for _ in range(t):
    n = int(input())
    print(*fibonacci(n))