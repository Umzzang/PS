n, k = map(int, input().split())
arr = [-1] * 100001
visited = [0] * 100001
arr[n] = 0
cnt = 0

def search(n, cnt):
    nm = n - 1
    np = n + 1
    nj = 2 * n
    if 0<=nm<=100000 and arr[nm] == -1 :
        arr[nm] = cnt + 1
        stack.append(nm)
        
    if 0<=np<=100000 and arr[np] == -1:
        arr[np] = cnt + 1
        stack.append(np)
        
    if 0<=nj<=100000 and arr[nj] == -1:
        arr[nj] = cnt + 1
        stack.append(nj)
        

stack = [n]

while stack and arr[k] == -1:
    # print(stack)
    n = stack.pop(0)
    
    search(n, arr[n])
    
    

print(arr[k])