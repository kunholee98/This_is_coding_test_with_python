# 실전 6-3. 두 배열의 원소 교체: N개의 원소를 가진 두 배열 A,B에서 K번 만큼 원소를 교체할 수 있다고 할 때, A의 원소의 합이 가장 크게끔 만들면 그 합은?
NK = list(map(int,input(">> ").split()))
N,K = NK[0],NK[1]
A = list(map(int,input(">> ").split()))
B = list(map(int,input(">> ").split()))
# print(A, B)
A.sort()    # 오름차순으로 정리하여 index가 낮은 순서로 K번째까지 B와 비교
B = sorted(B, reverse=True) # B는 내림차순으로 정리하여 index가 낮은 순서로 A와 교체
for i in range(K):
    if A[i] < B[i]:
        A[i] = B[i] # A에서 가장 작은 element가 B에서 가장 큰 element보다 작다면 교체, 아니라면 break
    else:
        break
print(sum(A))