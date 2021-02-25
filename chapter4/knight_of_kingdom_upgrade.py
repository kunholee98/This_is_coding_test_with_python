# 실전 2-1. 왕실의 나이트: 8 x 8 체스판에서 나이트의 위치를 입력받은 후, 나이트가 움직일 수 있는 경우의 수를 출력. // 기재되어 있는 정답은 dx, dy를 set, list를 이용하여 품.
def count_way(knight):  # 나이트가 움직일 수 있는 경우를 세는 함수
    x,y = knight[0], knight[1]      # c1 이 입력되면 x = 'c', y = 1
    count = 0
    way = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)] # 나이트가 움직일 수 있는 경우의 수
    row = [1,2,3,4,5,6,7,8]                                         # row * column, 체스판의 모든 좌표
    column = ['a','b','c','d','e','f','g','h']
    for dx,dy in way:
        if chr(ord(x)+dx) in column and y+dy in row:    # x+dx, y+dy가 나이트가 움직인 후의 좌표이며, row와 column 안에 존재하면 카운트
            count += 1
    return count                    # 8가지의 경우를 모두 고려한 후 카운트 결과를 리턴.

knight = list(input(">> "))
knight[1] = int(knight[1])
result = count_way(knight)
print(result)
