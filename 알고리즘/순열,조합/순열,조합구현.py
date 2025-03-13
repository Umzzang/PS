from itertools import permutations, combinations

arr = [1, 2, 3, 4]
# 모듈 사용


print(list(combinations(arr, 2)))


print(list(permutations(arr, 2)))


# 구현

# 조합
arr = [1, 2, 3, 4, 5]

def com(arr:list, n):
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in range(len(arr)):
            result.append([arr[i]])
    else:
        for i in range(len(arr)- n + 1):
            for j in com(arr[i+1:], n-1):
                result.append([arr[i]] + j)
    return result

def com1(arr:list, n):
    pass

# 순열

def per(arr:list, n):
    result = []
    if n > len(arr):
        return result
    
    if n == 1:
        for i in arr:
            result.append([i])
    else:
        for i in range(len(arr)):
            ans = [j for j in arr]
            ans.remove(arr[i])
            for j in per(ans, n-1):
                result.append([arr[i]] + j)
    return result



print(com(arr, 3))
print(per(arr, 3))


