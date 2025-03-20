n = int(input())

dp = [3]
i = 0

while dp[i] < n:
    i+=1
    before = dp[-1]
    dp.append(before * 2 + i+3)




             
def search(n, i):
    count = i+3

    if n == 1:
        return 'm'
    elif n== 2:
        return 'o'
    elif n==3:
        return 'o'

    if n <= dp[i-1]:
        return search(n, i-1)
    elif n <= dp[i-1] + count:
        if n - dp[i-1] == 1:
            return 'm'
        else:
            return 'o'
    else:
        # return search(x-middle-half, i-1)


        return search(n-count-dp[i-1], i-1)


# print(dp, i)
print(search(n, i))

