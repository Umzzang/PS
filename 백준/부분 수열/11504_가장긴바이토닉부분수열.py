import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))


def d(index):
    dp = [0]
    dp2 = [0] 
    

    for i in range(index+1):
        if dp[-1] < arr[i]:
            dp.append(arr[i])
        else:
            start = 0
            end = len(dp)
            while start < end:
                mid = (start + end)//2
                if dp[mid] > arr[i]:
                    end = mid
                    
                else:
                    start = mid + 1
            dp[end] = arr[i]
    
    for i in range(n-1, index-1, -1):
        if dp2[-1] < arr[i]:
            dp2.append(arr[i])
        else:
            start = 0
            end = len(dp2)
            while start < end:
                mid = (start + end)//2
                
                if dp2[mid] > arr[i]:
                    end = mid
                else:
                    start = mid + 1
            dp2[end] = arr[i]
    return len(dp) - 1 + len(dp2) -1 -1

    # for j in range(n-1, -1, -1):
    #     for k in range(n-1, j, -1):
    #         if arr[k] < arr[j]:
    #             dp2[j] = max(dp2[j], dp2[k] + 1)
    # # print(dp, dp2)




    # return dp[-1] + dp2[i] - 1



cnt = []


if n == 1 or n == 2:
    print(n)
else:
    for i in range(n):
        cnt.append(d(i))

    print(max(cnt))