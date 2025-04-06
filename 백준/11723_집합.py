import sys
input = sys.stdin.readline


def main():
    m = int(input())
    lst = set()
    for _ in range(m):
        order = input().rstrip()
        if order == 'all':
            lst = set()
            for i in range(1, 21):
                lst.add(i)
        elif order == 'empty':
            lst = set()
        else:
            order,x = order.split()
            # print(order, x)
            x = int(x)
            if order == 'add':
                lst.add(x)
            elif order == 'remove':
                try:
                    lst.remove(x)
                except:
                    continue
            elif order == 'check':
                if x in lst:
                    print(1)
                else:
                    print(0)
            elif order == 'toggle':
                if x in lst:
                    lst.remove(x)
                else:
                    lst.add(x)
        
        


if __name__ == "__main__":
    main()