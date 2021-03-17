# 실전 8-3. 바닥공사: 2*N의 모양의 바닥이 주어질 때, 1*2, 2*1, 2*2 타일로 바닥을 덮을 수 있는 경우의 수를 구하여라 (너무 커질 수 있으므로 796796으로 나눈 나머지를 출력하자)
N = int(input(">> "))
memo = list(range(N+1))
for i in range(len(memo)):
    if i == 0 or i == 1:
        memo[i] = 1
    else:
        memo[i] = memo[i-2]*2 + memo[i-1]
print(memo[N]%796796)