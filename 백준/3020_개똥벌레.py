import sys

def check(height, arr):
    # print(arr, height)
    l = 0
    r = len(arr)-1
    while l<=r:
        mid = (l+r)//2
        if arr[mid] < height:
            l = mid + 1
        elif arr[mid] >= height:
            r = mid -1
    return len(arr) - (r+1)



def main():
    input = sys.stdin.readline
    n, h = map(int, input().split())
   
    
    ground = []
    top = []
    for i in range(n):
        if i % 2 == 0:
            ground.append(int(input()))
        else:
            top.append(int(input()))
    
    ground.sort()
    top.sort()
    answer = n
    cnt = 0
    for i in range(1, h+1):
        l_cnt = check(i, ground)   #1  2
        r_cnt = check(h-i+1, top)  #7  6
        # print(i, l_cnt, r_cnt)
        total_cnt = l_cnt + r_cnt
        if total_cnt < answer:
            answer = total_cnt
            cnt = 1
        elif total_cnt == answer:
            cnt += 1
    print(answer, cnt)



    # 부분합
    # ground = [0] * (h+1)
    # top = [0] * (h+1)
    # for i in range(n):
    #     tmp = int(input())
    #     if i%2 == 0:
    #         ground[tmp] += 1
    #     else:
    #         top[tmp] += 1

    # for i in range(h-1, 0, -1):
    #     ground[i] += ground[i+1]
    #     top[i] += top[i+1]
    # # print(ground, top)
    # answer = n
    # cnt = 1
    # for i in range(1, h+1):
    #     s = ground[i] + top[h-i+1]
    #     # print(i, s)
    #     if s < answer:
    #         answer = s
    #         cnt = 1
    #     elif s == answer:
    #         cnt += 1
    # print(answer, cnt)
    
    

   


if __name__ == "__main__":
    main()