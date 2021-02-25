# 실전 1-3. 1이 될때까지: 수를 입력받으면 1을 빼주거나 k로 나누어주는 두가지 방법을 통해 1을 만든다. 이때 가장 적은 횟수로 1을 만들기 위해 필요한 계산 횟수는?
num,k = map(int,input(">> ").split())
count = 0
temp = 0
while num > k:  # k로 나누어 떨어지면 count에 1을 더하고 (temp = 1), 만약 나머지가 생긴다면 나머지+1을 count에 더한다. (temp = 나머지+1)
                #나머지+1은 다시 나누어떨어질때까지 1을 빼주어야하는 과정을 생략한 것.
    num,temp = num//k, num%k+1
    count += temp
    print(num,count)
count += num-1
print(count)