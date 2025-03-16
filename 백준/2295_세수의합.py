import sys
input = sys.stdin.readline

n = int(input())
nlst = []
# ndict = {}
for _ in range(n):
    v = int(input())
    nlst.append(v)
    # ndict[v] = 1

nlst.sort()
nlst2 = set()
for i in range(n):
    for j in range(i, n):
        nlst2.add(nlst[i] + nlst[j])

# nlst2 = sorted(list(nlst2))

# print(nlst2)
def search(target): # target 1 3
    start = 0
    end = len(nlst2)
    while start <= end:
        mid = (start+end)//2
        m = nlst2[mid]
        if m == target:
            
            return 1
        elif m < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

answer = -1
for i in range(n-1, -1, -1):
    for j in range(i):
        target = nlst[i]-nlst[j]
        # print(nlst[i], nlst[j], i, j, target)

        if target in nlst2:
            answer = i
            break

        # if search(target):
        #     answer= i
        #     break
    if answer != -1:
        break
print(nlst[i])
