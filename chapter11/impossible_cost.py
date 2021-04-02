# 4. 만들 수 없는 금액: 다양한 금액의 동전이 n개 주어질 때, 이를 이용하여 만들 수 없는 최소 금액은?
import sys

n = int(input())
coins = list(map(int, sys.stdin.readline().split()))
coins.sort()
target = 1
for i in coins:
    if i <= target:
        target += i
    else:
        break
print(target)