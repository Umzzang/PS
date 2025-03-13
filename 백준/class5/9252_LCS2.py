a = input()
b = input()

graph = [[0] * (len(b)+1) for _ in range(len(a)+1)]
maxv = 0
ans = ''
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            graph[i+1][j+1] = graph[i][j] + 1
            if maxv < graph[i][j] + 1:
                maxv = graph[i][j] + 1
        else:
            graph[i+1][j+1] = max(graph[i][j+1], graph[i+1][j])


if maxv != 0:
    i = len(a)
    j = len(b)
    while i >= 0 and j >= 0:
        start = graph[i][j]
        if graph[i-1][j] == graph[i][j]:
            i -= 1
        elif graph[i][j-1] == graph[i][j]:
            j -= 1
        else:
            ans = a[i-1] + ans
            i -= 1
            j -= 1





if maxv == 0:
    print(maxv)
else:
    print(maxv)
    print(ans)