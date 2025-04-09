import sys

input = sys.stdin.readline



def score(a,b,c,d):
    s = 0
    s += a + 2*b + 4*c + 8 *d
    return s

def rotate(arr, d):
    if d == 1:
        return [arr[-1]] + arr[:7]
    elif d == -1:
        return arr[1:8] +[arr[0]]
    else:
        return arr

def check(arrlst, i, d):
    answer = [0] * 4
    # answer[i-1] = d
    result = []
    for j in range(1, 4):
        result.append(compare(arrlst[j], arrlst[j+1]))
    print(result)
    visited = [0] * 4
    q = [(i-1, d)]
    visited[i-1] = 1
    while q:
        x, d = q.pop(0)
        answer[x] = d
        # print('???', answer)
        for j in (-1, 1):
            nx = x + j
            if 0<=nx<4 and visited[nx] == 0:
                if j == 1:
                    if result[nx-1]:
                        q.append((nx, d*-1))
                    else:
                        q.append((nx, 0))
                else:
                    if result[nx]:
                        q.append((nx, d*-1))
                    else:
                        q.append((nx, 0))
                visited[nx] = 1
    # print(answer)
    return answer

    


def compare(flst, slst):
    if flst[2] != slst[6]:
        return True
    else:
        return False



def main():
    first = list(map(int, input().rstrip()))
    second = list(map(int, input().rstrip()))
    third = list(map(int, input().rstrip()))
    fourth = list(map(int, input().rstrip()))
    # print(first)
    k = int(input())
    
    for _ in range(k):
        top = [0, first, second, third, fourth]
        n, d = map(int, input().split())
        a, b, c, d = check(top, n, d)
        print(a,b,c,d)
        first, second, third, fourth = rotate(first, a), rotate(second, b), rotate(third, c), rotate(fourth,d)
        print(first, second,third,fourth)
    print(score(first[0], second[0], third[0], fourth[0]))
if __name__ == "__main__":
    main()