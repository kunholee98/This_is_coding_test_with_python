# 실전 8-4. 효율적인 화폐 구성: 화폐의 단위가 N개 주어지면 이를 이용해 M원을 만들 수 있는 최소 화폐 개수를 구하여라. 못구하면 -1을 출력하라.
NM = list(map(int, input(">> ").split()))
N,M= NM[0],NM[1]
money = list(range(N))
for i in range(len(money)):
    money[i] = int(input(">> "))
result = [12345]*(M+1)
print(result)
for i in money:     # try & except문으로 주어진 M보다 화폐의 단위가 더 클 경우 index의 범위를 넘어서는 경우를 무시하였음.
    try:
        result[i] = 1
    except:
        pass
for i in range(len(result)):    # i = 6, j = 2, 3 인 경우, 먼저 j=2일때 result[4]+1(=3)과 result[6](=12345) 중 더 작은 값이 result[6]에 저장됨.
    for j in money:             # j=3일때 result[3]+1(=2) 과 result[6](=3) 중 더 작은 값이 result[6]에 저장됨. 이를 통해 i원을 만들 수 있는 최소 값이 저장됨.
        if i > j:               # 만들 수 없는 경우 12345가 그대로 저장되어 있음.
            result[i] = min(result[i-j]+1, result[i])
print(result[M] if result[M]<10001 else -1)