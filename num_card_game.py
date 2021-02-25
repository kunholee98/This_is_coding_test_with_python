# 실전 1-2. 숫자 카드 게임
N,M = map(int, input(">> ").split())    # 행렬의 크기를 입력받음.
card = [[0]*M for i in range(N)]        # 1에서 입력받은 크기로 card 행렬을 만듦.
result = 0
for i in range(N):
    card[i] = sorted(list(map(int, input(">> ").split())))  # 각 행의 카드 값들을 리스트 형식으로 입력 받음과 동시에 sorted() 함수를 이용하여 오름차순으로 정렬.
                                                            # 각 행의 첫 항들이 최소값임을 이용하기 위해서 오름차순을 택함.
for i in range(N):  # 각 행의 첫 항들의 크기를 비교하며 가장 큰 값을 찾아서 출력.
    if card[i][0] >= result:
        result = card[i][0]

print(result)
