# 실전 8-1. 1로 만들기: 1) 5로 나누기, 2) 3으로 나누기, 3) 2로 나누기, 4) 1 빼기를 반복하여 최종적으로 1이 나올 수 있도록 하는 연산의 최소 횟수는?
X = int(input(">> "))
i=0
memo = {}
while not X in memo:    # memorization을 이용하여 우선 각 수가 1씩 더했을때의 연산 횟수를 입력해놓는다. make1 함수를 통해 이보다 적은 횟수로 해당 숫자를 만들 수 있다면 업데이트 하는 형식으로
    i+=1                # 4 * 30000 번 이내의 연산으로 해결가능하다.
    memo[i] = i-1
    #print(memo)

def make1(x):   # x = 2라면 3,4,6,10를 연산의 역을 통해 만들 수 있으며, memo[2]+1의 횟수로 만들 수 있으므로 이를 업데이트.
    if x >= X:
        return
    temp = memo[x]
    if temp + 1 < memo[x+1]:
        memo[x+1] = temp +1
    if 2*x <= X and temp+1 < memo[2*x]:
        memo[2*x] = temp+1
    if 3*x <= X and temp+1 < memo[3*x]:
        memo[3*x] = temp+1
    if 5*x <= X and temp+1 < memo[5*x]:
        memo[5*x] = temp+1    

for i in memo:
    #print(i)
    make1(i)
    #print(memo)
print(memo[X])

