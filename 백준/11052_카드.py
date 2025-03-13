n = int(input())

card = [0] + list(map(int, input().split()))

answer = [0] * (n+1)




# answer[1] = card[1]
for i in range(1, n+1):
    for j in range(1, i+1):
        answer[i] = max(answer[i-j] + card[j], answer[i])

print(answer[n])
# print(answer)