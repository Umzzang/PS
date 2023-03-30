import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [i for i in range(n+1)]
cnt, *cntl = map(int, input().split())

def find_root(x):
    if arr[x] == x:
        return x
    else:
        arr[x] = find_root(arr[x])
        return arr[x] 
    
def union_root(x, y):
    x = find_root(x)
    y = find_root(y)

    if x != y:
        arr[x] = y

partylst = []


for i in range(1, len(cntl)):
    union_root(cntl[i-1], cntl[i])

for _ in range(m):
    pc, *pcl = map(int, input().split())
    partylst.append(pcl)
    for i in range(1, len(pcl)):
        union_root(pcl[i-1], pcl[i])


for i in range(1, n+1):
    arr[i] = find_root(i)

cntt = 0
if cnt > 0:
    for i in range(1, n+1):
        if arr[cntl[0]] != arr[i]:
            arr[i] = False
else:
    cntt = m


for i in range(m):
    for p in partylst[i]:
        if arr[p] != False:
            break
        else:
            cntt += 1
            break
    
            
# print(arr)

print(cntt)
