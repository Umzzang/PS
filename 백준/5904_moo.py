n = int(input())

dp = [3]
i = 0
# m = [0]
while dp[i] <=n:
    i+=1
    before = dp[-1]
    dp.append(before * 2 + i+3)
    # new = []
    # for data in m:
        # new.append(data+dp[-2]+i+3)

    # m.append(before)
    # m += new

print(dp, i)

def search(x, i): # 11 2
    # if not dp:
    #     return 'm'
    print(x,i)
    if x == 1:
        return 'm'
    elif x == 2:
        return 'o'
    elif x== 3:
        return 'o'

    count = i + 3
    if dp[i-1] + count > x:
        if x ==dp[i-1] + 1:
            return 'm'
        else:
            return 'o'
    elif dp[i-1] + count < x:
        return search(x-count-dp[i-1], i-1)
    else:
        return 'o'


print(search(n, i))

