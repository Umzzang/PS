
def search(l, r, cut, arr):
    ans = 0
    while l <= r:
        
        mid = (l+r)//2
        now = arr[0]
        answer = []
        cnt = 0

        for i in range(1, len(arr)-1):
            # print(arr[i], now)
            
            if arr[i] - now >= mid and arr[len(arr)-1] - arr[i] >= mid:
                answer.append(arr[i]- now)
                now = arr[i]
                cnt += 1
        if arr[len(arr)-1] - now >= mid:
            answer.append(arr[len(arr)-1] - now)
            
        
        if cnt >= cut:
            l = mid + 1
            if ans < min(answer):
                ans = min(answer)
        elif cnt < cut:
            r = mid -1
        
        # print(mid, cnt, answer, ans)
    return ans


def main():
    n, m, len = map(int, input().split())
    cake = []
    
    for _ in range(m):
        cake.append(int(input()))
    cake = [0] + cake + [len]
    for _ in range(n):
        cut = int(input())
        
        print(search(1, len, cut, cake))

    



if __name__ == "__main__":
    main()