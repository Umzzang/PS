import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

ino = list(map(int, input().split()))
posto = list(map(int, input().split()))
pre = []
fi = [0] * (n+1)
for i in range(n):
    fi[ino[i]] = i
def divide(l_first, l_last, r_first, r_last):
    # print(arr1, arr2)
    global pre
    if  l_first > l_last or r_first > r_last:
        return
    
    
    root = posto[r_last]
    # print(root)
    # print([l_first, l_last, r_first, r_last])
    index = fi[root]
    leftNum = index - l_first
    rightNum = l_last - index 
    print(root, end=' ')

    divide(l_first, l_first + leftNum - 1, r_first, r_first + leftNum-1)
    divide(l_last - rightNum + 1, l_last, r_last-rightNum, r_last-1)

divide(0, n-1, 0, n-1)

# print(pre)
# print(*pre)
