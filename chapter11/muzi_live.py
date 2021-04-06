# 6. 무지의 먹방 라이브: food_times로 무지가 먹어야할 음식 리스트(먹는데 필요한 시간이 입력되어 있음)가 주어질 때,
# k초 후에 몇 번에 있는 음식을 먹고 있는지 출력(음식을 모두 먹었다면 -1)
import sys

def solution (f, k):
    i = 0
    length = len(f)
    check = [0] * length
    #print(check)
    if sum(f) <= k:
        return -1
    while k > 0:
        i %= length
        if f[i] == 0:
            check[i] = 1
        if check[i] == 0:
            f[i] -= 1
            k -= 1
        i+=1
    i %= length
    while f[i] == 0:
        i %= length
        i += 1
    return i+1
            

food_times = list(map(int,sys.stdin.readline().split()))
k = int(input("k: "))
print(solution(food_times,k))