import sys
from math import sin
input = sys.stdin.readline

def func(a,b,c,v):
    return a*v + b*sin(v)-c



def main():
    a, b, c = map(int, input().split())
    left = c/a -b
    right = c/a + b
    
    while left <= right:
        mid = (left + right) / 2
        value = func(a,b,c,mid)
        # print(mid, value)
        if -10**(-9) <= value <= 10**(-9):
            print(mid)
            break
        elif value < 0:
            left = mid
        else:
            right = mid

if __name__ == "__main__":
    main()