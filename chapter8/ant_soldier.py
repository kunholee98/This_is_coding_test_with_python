# 개미 전사: N size의 식량창고 리스트가 주어질 때, 인접한 식량 창고를 털 수 없는 조건에서 얼마나 많은 식량을 훔칠 수 있겠는가?
N = int(input(">> "))   # 3~100
K = list(map(int,input(">> ").split())) # 0~1000
sum = 0
for i in range(len(K)):
    if i == 0 or i == 1:
        continue
    else:
        K[i] = max(K[i]+K[i-2], K[i-1])
print(K[-1])