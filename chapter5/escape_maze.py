# 실전 5-2. 미로 탈출: (0,0)에서 (N,M)까지 괴물(0)을 피해 탈출할 수 있는 길(1)의 최소 길이를 구하시오.
from collections import deque   # bfs를 쓰기 위해서 deque 모듈을 호출
def bfs(i,j):
    queue = deque()         # 큐 선언
    queue.append([i,j])     # 큐에 현 좌표 저장
    while queue:            # 큐가 비어있지 않다면
        i,j = queue.popleft()       # 좌표 하나를 pop시키고 그 값을 i,j로 저장
        print("location: ({},{})".format(i,j))  # i,j 현 좌표 출력
        if i < N-1 and maze[i+1][j] == 1:   # 현 좌표에서 아래의 값이 1이라면(한 번도 방문하지 않은 위치)
            queue.append([i+1,j])           # 큐에 그 위치를 넣고
            maze[i+1][j] = maze[i][j] +1    # 해당 위치의 값을 1 추가 (길의 길이를 의미)
            print("아래로")                 # 큐에 넣은 값의 방향을 보여줌
        if j < M-1 and maze[i][j+1] == 1:
            queue.append([i,j+1])
            maze[i][j+1] = maze[i][j] +1
            print("오른쪽으로")
        if i > 0 and maze[i-1][j] == 1:
            queue.append([i-1,j])
            maze[i-1][j] = maze[i][j] +1
            print("위로")
        if j > 0 and maze[i][j-1] == 1:
            queue.append([i,j-1])
            maze[i][j-1] = maze[i][j] +1
            print("왼쪽으로")
        print("queue",queue)
        if i+1 == N and j+1 == M:       # 만약 마지막 좌표에 도착했다면 maze[N-1][M-1]을 리턴
            return maze[i][j]           # 그 값이 출발선부터의 길이를 의미
        #for k in range(len(maze)):
        #    print(maze[k])


# 미로 정보 입력
N,M = map(int, input("N, M: ").split())
maze = []
for i in range(N):
    maze.append(list(map(int,input(">> "))))
way = bfs(0,0)
print("length of the way: ",way)