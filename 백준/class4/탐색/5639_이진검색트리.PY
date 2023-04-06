import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
tree = []




while True:
    try:
        tree.append(int(input()))
    except:
        break



def post(start, end):
    if  start > end:
        return
    # if start == end:
    #     print(tree[start])
    #     return
    # print(start, end)
    root = tree[start]
    leftindex = end + 1
    for i in range(start+1, end+1):
        if tree[i] > root:
            leftindex = i
            break
    
    # print(root, leftindex)
    post(start+1, leftindex-1)
    post(leftindex, end)
    print(root)



post(0, len(tree)-1)