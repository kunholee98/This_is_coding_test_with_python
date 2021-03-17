# 실전 9-1. 미래 도시: N개의 회사, M개의 경로가 존재. K번 도시를 거쳐 X번 도시를 가고 싶을 때 길을 최소로 이용하는 횟수를 출력하라. 길이 없으면 -1 출력
N,M = map(int,input("N,M : ").split())
way = [[0]*N for i in range(N)]     # way (2-dimension lst 초기화)
fastway = [100]*N
print(way)
for i in range(M):
    temp = list(map(int,input("way {} : ".format(i)).split()))
    print(temp)
    way[temp[0]-1][temp[1]-1] = 1
X,K = map(int,input("X,K : ").split())
fastway[0] = 0
# 시작점과 각 도시의 거리를 fastway에 저장 (1->X 까지의 최단거리를 구하기)
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        elif way[i][j] == 1:
            fastway[j] = min(fastway[i]+1, fastway[j])
print(fastway)

# K까지 갈 수 없다면 -1 리턴 후 종료
if fastway[K-1] == 100:
    print(-1)
    exit()

# 1 -> K 까지의 거리 저장 및 fastway 초기화, K지점을 기준으로 지정
result = fastway[K-1]
print(result)
fastway = [100]*N
fastway[K-1] = 0

# K -> X 최단 거리, K부터 N, 1부터 K-1 까지 탐색 / way[숫자가 작은 곳][숫자가 큰 곳] 형식으로 길을 저장해 놓았기 때문에 min,max를 이용
for i in range(K-1,K+N-1):
    for j in range(K-1,K+N-1):
        i %= N
        j %= N
        a = min(i,j)
        b = max(i,j)
        if i==j:
            continue
        elif way[a][b] == 1:
            fastway[j] = min(fastway[i]+1, fastway[j])

# X까지 갈 수 없다면 -1 리턴 후 종료
if fastway[K-1] == 100:
    print(-1)
    exit()
print(fastway)
result += fastway[X-1]
print(result)