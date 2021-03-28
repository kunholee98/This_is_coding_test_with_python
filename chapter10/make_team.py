# 실전 10-1. 팀 결성: 0번부터 N번까지의 학생 N+1명이 있을 때, '팀 합치기', '같은 팀 여부 확인' 연산을 M회 진행하여 결과를 출력
import sys

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a,b):
    #팀을 합칩니다.
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def check(a,b):
    #같은 팀인지 확인합니다.
    if parent[a] == parent[b]:
        return "YES"
    return "NO"

N,M = map(int,input(">> ").split())
table = list(range(M+1))
parent = list(range(M+1))

for i in range(M):
    a,b,c = map(int,sys.stdin.readline().split())
    table[i] = (a,b,c)

for i in range(M):
    key = table[i][0]
    # 팀 합치기
    if key == 0:
        union(table[i][1], table[i][2])
    # 같은 팀 여부 확인
    else:
        print(check(table[i][1], table[i][2]))