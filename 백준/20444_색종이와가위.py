def main():
    n, k = map(int, input().split())
    l = 0
    r = n//2 + 1
    while l <= r:
        mid = (l+r) // 2 
        tmp = (mid + 1) * (n - mid + 1)
        if tmp == k:
            print("YES")
            break
        elif tmp > k:
            r = mid -1
        elif tmp <k:
            l = mid + 1
    if l > r:
        print("NO")



if __name__ == "__main__":
    main()