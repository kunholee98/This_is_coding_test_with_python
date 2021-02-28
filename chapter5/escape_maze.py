# 실전 5-2. 미로 탈출: (0,0)에서 (N,M)까지 괴물(0)을 피해 탈출할 수 있는 길(1)의 최소 길이를 구하시오.
from collections import deque
def bfs(i,j,count):
    queue = deque([])
    maze[i][j] = 0
    if i > 0 and maze[i-1][j] == 1:
        queue.append((i-1,j))
    if i < N and maze[i+1][j] == 1:
        queue.append((i+1,j))
    if j > 0 and maze[i][j-1] == 1:
        queue.append((i,j-1))
    if j < M and maze[i][j+1] == 1:
        queue.append((i,j+1))
    count += 1                          
    # TODO: queue를 이용하는 방법에 대해 좀 더 고민해봐야 할듯.
    for x,y in queue:
        bfs(x,y,count)
        queue.popleft()


# 미로 정보 입력
N,M = map(int, input("N, M: ").split())
maze = []
for i in range(N):
    maze.append(list(map(int,input(">> "))))
count = 0
bfs(0,0,count)
print(count)