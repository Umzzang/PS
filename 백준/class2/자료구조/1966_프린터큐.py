c = int(input())
for i in range(c):
    n, m = map(int, input().split(' '))
    lst = list(map(int, input().split(' ')))
    lst2 = [0 for _ in range(n)]
    lst2[m] = 1
    cnt = 0
    while True:
        if lst[0] == max(lst):
            cnt += 1
            if lst2[0] == 1:
                print(cnt)
                break
            else:
                del lst[0]
                del lst2[0]
        else:
            lst.append(lst.pop(0))
            lst2.append(lst2.pop(0))