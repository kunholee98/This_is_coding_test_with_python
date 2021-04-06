# 6. 무지의 먹방 라이브: food_times로 무지가 먹어야할 음식 리스트(먹는데 필요한 시간이 입력되어 있음)가 주어질 때,
# k초 후에 몇 번에 있는 음식을 먹고 있는지 출력(음식을 모두 먹었다면 -1)
import sys
import copy
import numpy as np

def solution (f, k):
    if sum(f) <= k:
        return -1
    f_copy = np.copy.deepcopy(f)
    # 여기서부터 더 풀면 됩니다~ 


food_times = list(map(int,sys.stdin.readline().split()))
k = int(input("k: "))
print(solution(food_times,k))