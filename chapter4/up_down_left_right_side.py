# 2. 상하좌우 문제
size = int(input('>> '))    # 지도의 크기를 입력
way = input('>> ').split()  # 가고자 하는 방향을 리스트로 입력받음
x,y = 1,1
for i in way:   # size를 토대로 만든 지도를 벗어나지 않도록 x,y의 값을 바꾸어줌.
    if i == 'R' and x < size:
        x += 1
    elif i == 'L' and x > 1:
        x -= 1
    elif i == 'U' and y > 1:
        y -= 1
    elif i == 'D' and y < size:
        y += 1
print("{} {}".format(x,y))