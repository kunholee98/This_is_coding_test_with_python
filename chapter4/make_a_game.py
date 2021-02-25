# 실전 2-2. 게임 개발: 평지와 바다로 이루어진 맵의 크기를 입력받고, 일정 규칙에 의해 움직이는 캐릭터가 움직일 수 있는 횟수를 구하시오.
N, M = map(int, input("N, M: ").split())
A, B, d = map(int, input("A, B, d: ").split())
# 육지 = 0, 바다 = 1 인 게임 지도 정보 받아오기
game_map = []
for i in range(N):
    game_map.append(list(map(int, input(">> ").split())))   # 육지 = 0, 바다 = 1
# 캐릭터가 이동한 경로 표시하는 지도 (가보지 않은 곳 = 0, 지나간 곳 = 1)
way = [[0]*M for i in range(N)]
# 캐릭터가 위치한 곳을 표시, 카운트
count = 1
way[A][B] = 1
rotate_count = 0
direction = d   # 북: 0, 동: 1, 남: 2, 서: 3
dx = [0, 1, 0, -1]  # direction을 index로 사용했을 때 캐릭터가 움직이는 거리 ex) direction = 0 일때 x = x, y = y-1 (북쪽으로 한칸 이동)
dy = [-1, 0, 1, 0]
game_map[A][B] = 1
while True:
    direction -= 1  # 북서남동 순으로 방향을 변경
    if direction < 0:   # 방향을 0 -> 3 으로 바꾸어주기위한 if문
        direction = 3
    x,y  = A + dx[direction], B + dy[direction] # 이동할 위치
    # print("dir: {}, x,y: {},{}".format(direction,x,y))    # 방향과 만약 이동을 하게 되었을 때의 위치
    if game_map[x][y] == 0 and way[x][y] == 0:  # 이동할 위치가 게임지도에서 육지이며 가보지 않은 곳일 경우, 카운트 및 경로에 표시
        count += 1
        A,B = x,y
        rotate_count = 0
        print("A,B = {},{}".format(B,A))
        way[x][y] = 1
        #for i in range(N): # 경로를 보여주기위한 for문
        #    print(way[i])
        continue
    rotate_count += 1   # 만약 움직이지 못했다면 회전 횟수를 카운트
    if rotate_count > 3:    # 4방면 모두 갈 수 없다면 회전 횟수 초기화 및 뒤로 이동
        rotate_count = 0
        x, y = A - dx[direction], B - dy[direction]
        if game_map[x][y] == 0: # 뒤 방향이 육지라면 뒤로 이동, else라면(바다라면) while 탈출
            A,B = x,y
        else:
            break
        
print(count)