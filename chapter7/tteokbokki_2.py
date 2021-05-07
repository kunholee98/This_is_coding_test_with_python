# 떡볶이 연습

def cut(tteoks, start, end, target, result):
    s = 0
    mid = (start+end)//2
    if start >= end:
        return result
    for tteok in tteoks:
        if mid > tteok:
            break
        s += tteok - mid
    if s == target:
        return mid
    elif s > target:
        return cut(tteoks, mid+1, end, target, mid)
    else:
        return cut(tteoks, start, mid-1, target, result)

import sys
n,m = map(int, input().split())
tteoks = list(map(int, sys.stdin.readline().split()))
tteoks.sort(reverse=True)
print(cut(tteoks, 0, tteoks[0], m, tteoks[0]))
