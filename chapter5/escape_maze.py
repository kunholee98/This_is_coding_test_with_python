# 실전 5-2. 미로 탈출: (0,0)에서 (N,M)까지 괴물(0)을 피해 탈출할 수 있는 길(1)의 최소 길이를 구하시오.
from collections import deque
def bfs(i,j,count):
    queue = deque()
    queue.append([i,j])
    while queue:
        i,j = queue.popleft()
        print(i,j)
        if i+1 == N and j+1 == M:
            return count
        maze[i][j] = 0
        if i > 0 and maze[i-1][j] == 1:
            queue.append([i-1,j])
            print("위로")
        if i < N-1 and maze[i+1][j] == 1:
            queue.append([i+1,j])
            print("아래로")
        if j > 0 and maze[i][j-1] == 1:
            queue.append([i,j-1])
            print("왼쪽으로")
        if j < M-1 and maze[i][j+1] == 1:
            queue.append([i,j+1])
            print("오른쪽으로")
        count += 1
        print("count",count,"queue",queue)
    # return count
    # TODO: count가 아니라 각 포인트에 값을 할당시켜서 거리를 봐야할듯?


# 미로 정보 입력
N,M = map(int, input("N, M: ").split())
maze = []
for i in range(N):
    maze.append(list(map(int,input(">> "))))
count = 0
count = bfs(0,0,count)
print(count)