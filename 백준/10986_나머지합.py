import sys

input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    nlsts = list(map(int, input().split()))
    slsts = [0] * n
    slsts[0] = nlsts[0]%m
    
    ncnt = {}
    
    ncnt[nlsts[0]%m] = 1
    for i in range(1, n):
        slsts[i] = (nlsts[i] + slsts[i-1])% m
        if ncnt.get(slsts[i]):
            ncnt[slsts[i]] += 1
        else:
            ncnt[slsts[i]] = 1
    
    
    answer = 0
    for i in range(m):
        if ncnt.get(i):
            if i == 0:
                answer += ncnt[i] * (ncnt[i] +1)//2
            else:
                answer += ncnt[i] * (ncnt[i] -1)//2
        
    print(answer)

    

if __name__ == "__main__":
    main()