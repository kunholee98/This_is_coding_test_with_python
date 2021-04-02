# 1. 모험가 길드: 공포도 x인 사람은 x명이 모여야만 모험을 떠날 수 있다. 모험을 떠날 수 있는 그룹의 최대 수를 구하시오
import sys

n = int(input(">> "))
adv = list(map(int,sys.stdin.readline().split()))
memo = {}
adv_i = []

for p in adv:
    if p not in memo:
        memo[p] = 1
        adv_i.append(p)
    else:
        memo[p] += 1
adv_i.sort()
cnt = 0
rest = 0
for i in adv_i:
    cnt += (memo[i]+rest) // i
    rest = (memo[i]+rest) % i   # 그룹을 만들고 남은 인원들은 다음 공포도를 갖고 있는 인원들과 함께 그룹을 만든다.
print(cnt)