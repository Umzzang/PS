n = int(input())

arr = [[1, 1], [1, 0]]
p = 1000000007
def mul(arr1, arr2):
    new_arr = [(arr1[0][0] * arr2[0][0] + arr1[0][1] * arr2[1][0])%p, (arr1[0][0] * arr2[0][1] + arr1[0][1] * arr2[1][1])%p], [(arr1[1][0] * arr2[0][0] + arr1[1][1] * arr2[1][0])%p, (arr1[1][0] * arr2[0][1] + arr1[1][1] * arr2[1][1])%p]

    return new_arr


def div(n):
    if n == 1:
        return arr
    # tmp로 결과 만든 후에 아래에 넣어야 함
    # 아니면 mul(div(n//2), div(n//2)) 이렇게하면 갈때마다 함수 호출이기때문에 시간 오래걸림
    tmp = div(n//2)
    if n % 2 == 0:
        return mul(tmp, tmp)
    else:
        return mul(mul(tmp, tmp), arr)

if n > 2:
    result = div(n-1)
    print(result[0][0])
elif n == 0:
    print(0)
else:
    print(1)


