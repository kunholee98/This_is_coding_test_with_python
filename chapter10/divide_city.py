# 실전 10-2. 도시 분할 계획: N개의 집과 M개의 도로가 있을 때, 도로 유지비를 최소한 사용할 수 있도록 집을 두 개의 그룹으로 나누고 그때의 최소 도로 유지비를 출력하라.
import sys

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N,M = map(int,input(">> ").split())
table = []
parent = list(range(N+1))

for i in range(M):
    # 간선 정보 얻기 / c를 이용하기 위해 순서를 앞으로 바꿈
    a,b,c = map(int,sys.stdin.readline().split())
    table.append((c,a,b))

table.sort()
large = 0
result = 0

for i in table:
    c,a,b = i
    # 부모가 다르다면(연결이 되어있지 않다면) 둘을 연결하고 그 간선의 길이를 누적. 이때 large에는 가장 큰 간선의 길이를 넣음
    if find_parent(a) != find_parent(b):
        union(a,b)
        result += c
        large = max(large,c)
print(result - large)