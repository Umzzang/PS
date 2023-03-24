t = int(input())
for test in range(1, t+1):
    
    card = [0] * 10
    n = int(input())
    clist = list(map(int, input()))
    for c in clist:
        card[c] += 1
    for i in range(9, -1, -1):
        if card[i] == max(card):
            print(f'#{test} {i} {card[i]}')
            break