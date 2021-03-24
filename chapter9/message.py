# 실전 9-2. 전보 : N개의 도시와 각 도시를 잇는 방향성이 존재하는 통로 M개가 있을 때, C도시에서 다른 도시에 긴급 메세지를 보내려한다. 받을 수 있는 도시의 수와 총 걸리는 시간은?
# N,M,C 입력
N,M,C = map(int,input(">> ").split())
# X,Y,Z 정보 수집 (X -> Y 통로가 존재하고, 걸리는 시간은 Z)
message = [[] for i in range(N+1)]
for i in range(M):
    X,Y,Z = map(int,input(">> ").split())
    message[X].append((Y,Z))
print(message)
# 최단 시간을 기록하는 array & 시작지점 초기화 & 방문여부 확인 array
way = [1001]*(N+1)
way[C] = 0
visited = [False]*(N+1)
visited[C] = True

for i in message[C]:
    way[i[0]] = i[1]
for i in range(N-1):
    for j in message:

# 다익스트라 알고리즘으로 푸는 중입니다.