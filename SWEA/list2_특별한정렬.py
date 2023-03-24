t = int(input())
# for tc in range(1, t+1):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     # print(arr)
#     arr.sort()
#     # print(arr)
#     answer = []
#     print(f'#{tc}', end=" ")
#     for i in range(5):
#         print(arr[n-1-i], end=" ")
#         print(arr[i], end=" ")
#         answer.append(arr[n-i-1])
#         answer.append(arr[i])
#     print()

# 선택 정렬
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(10):
        iv = i
        if i % 2:
            for j in range(i, n):
                if arr[j] < arr[iv]:
                    iv = j
        else:
            for j in range(i, n):
                if arr[j] > arr[iv]:
                    iv = j
        arr[i], arr[iv] = arr[iv], arr[i]
    print(f'#{tc}', end=" ")
    print(*arr[:10])