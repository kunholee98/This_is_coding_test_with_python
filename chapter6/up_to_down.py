# 실전 4-1. 위에서 아래로: 크기에 상관없이 나열되어 있는 배열을 큰 수부터 작은 수의 순서로 정렬하시오!
lst = sorted(list(map(int,input().split())))    # 수의 배열을 받음과 동시에 오름차순으로 정렬
print(" ".join(str(i) for i in lst))            # join 함수를 이용하여 각 요소들 사이에 띄어쓰기가 들어감.