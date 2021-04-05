# 5. 볼링공 고르기: 1~M까지 다양한 무게의 볼링공이 N개 존재한다. 이때, 무게가 서로 다른 두 개의 공을 고르는 경우의 수는? (무게가 같더라도 모두 다른 공으로 취급한다.)
import sys
import copy

N,M = map(int,input(">> ").split())
lst = list(map(int, sys.stdin.readline().split()))
lst2 = copy.deepcopy(lst)
cnt = 0
for a in lst:
    del lst2[0]
    for b in lst2:
        if a != b:
            print(a,b)
            cnt +=1
print(cnt)