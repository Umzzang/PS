from collections import deque

def main():
    global visited, answer, computers
    ######## 입력 #############
    cnt_computer = int(input())
    cnt_link = int(input())
    visited = [0] * (cnt_computer + 1)
    computers = [[] for _ in range(cnt_computer + 1)]
    # print(visited)
    for _ in range(cnt_link):
        fir, sec = map(int, input().split(' '))
        computers[fir].append(sec)
        computers[sec].append(fir)
    ###############################
    
    sol = 1
    answer = 0
    # print(computers)
    if sol == 0:
        recursive(1)
    elif sol == 1:
        bfs(1)

    print(answer-1)

    
def recursive(now_computer):
    global answer
    if visited[now_computer] == 1:
        return 
    answer += 1
    visited[now_computer] = 1
    for com in computers[now_computer]:
        recursive(com)
    

def bfs(now_computer):
    global answer
    queue = deque()
    queue.append(now_computer)
    answer += 1
    visited[now_computer] = 1
    while queue:
        nc = queue.popleft()
        # answer += 1
        for com in computers[nc]:
            if visited[com] == 0:
                queue.append(com)
                visited[com] = 1
                answer += 1


    
    





if __name__ == "__main__":
    main()