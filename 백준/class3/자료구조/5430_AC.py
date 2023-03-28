import sys
input = sys.stdin.readline

t = int(input())
for tc in range(1, t+1):
    p = input()
    n = int(input())
    arr = input()[1:-2]
    if len(arr) == 0:
        arr = []
    else:
        arr = list(map(int, arr.split(',')))

    s = 0
    e = len(arr) - 1
    r = False
    flag = 0
    for function in p.rstrip():
        
        # print(function, e)
        if function == "R":
            r = not r
        else:
            if e < s:
                flag = 1
                break
            if r == False:
                s += 1
            elif r == True:
                e -= 1
            
    ans = ''
    if flag == 1:
        print('error')
    else:
        ans = '[' + ans
        if r == False:
            arr = arr[s:e+1]
            
        else:
            if s == 0:
                arr = arr[e::-1]
               
            else:
                arr = arr[e:s-1:-1]
                
        for a in arr:
            ans += str(a) +','
        if len(arr) == 0:
            ans += ']'
        else:
            ans = ans[:-1]+']'
            
        print(ans)