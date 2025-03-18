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
    middle = i + 3
    half = dp[i-1]

    if x <= half:
        return search(x, i-1)
    elif x < half + middle:
        if x -middle == 1:
            return 'm'
        else:
            return 'o'
    else:
        return search(x-middle-half, i-1)




print(search(n, i))

