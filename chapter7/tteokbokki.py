# 실전 7-2. 떡볶이 떡 만들기: 길이가 일정하지 않은 N개의 떡을 H cm로 자를 수 있는 절단기를 이용해 자른다. 이때, 잘려진 떡의 길이 총합이 M이 되도록하는 H는?
NM = list(map(int, input(">> ").split()))
N,M = NM[0], NM[1]
lst = sorted(list(map(int, input(">> ").split())), reverse=True)
memo = {}
result = 0
H = max(lst)
for num in lst:
    if not num in memo:
        memo[num] = 1
    else:
        memo[num] += 1
print(memo)
while result < M:
    result = 0
    H -= 1
    for length in memo:
        #print("length",length)
        if length > H:
            result += (length - H) * memo[length]
            #print("cut! with ", length)
    #print("H",H)
    #print("result",result)
print(H)

# 내림차순으로 정리한 후, H를 max(lst)부터 1씩 줄여나가면서 구하기!