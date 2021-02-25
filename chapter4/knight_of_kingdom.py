# 실전 2-1. 왕실의 나이트: 8 x 8 체스판에서 나이트의 위치를 입력받은 후, 나이트가 움직일 수 있는 경우의 수를 출력. // 기재되어 있는 정답은 dx, dy를 set, list를 이용하여 품.
def count_way(knight):  # 나이트가 움직일 수 있는 경우를 세는 함수
    x,y = knight[0], knight[1]      # c1 이 입력되면 x = 'c', y = 1
    count = 0
    row = [1,2,3,4,5,6,7,8]                         # row와 column의 조합으로 체스판의 모든 위치의 경우의 수를 나타낼 수 있다.
    column = ['a','b','c','d','e','f','g','h']
    if chr(ord(x)-2) in column:     # 먼저 나이트를 위로 2칸 이동하면 chr(ord(x)-2) = 'a' 이므로 column 안에 존재.
        if y+1 in row:              # 좌우로 1칸씩 나이트를 움직이면 우측으로 1칸 이동한 경우만 존재.
            count += 1
        if y-1 in row:              # 좌측으로 이동한 경우는 존재하지 않으므로 카운트를 하지 않음.
            count += 1
    if chr(ord(x)-1) in column:     # 나이트를 위로 1칸 이동.
        if y+2 in row:              # 좌우로 2칸씩 이동시켜 체스판 위에 존재하는 경우 카운트.
            count += 1
        if y-2 in row:
            count += 1
    if chr(ord(x)+1) in column:
        if y+2 in row:
            count += 1
        if y-2 in row:
            count += 1
    if chr(ord(x)+2) in column:
        if y+1 in row:
            count += 1
        if y-1 in row:
            count += 1
    return count                    # 8가지의 경우를 모두 고려한 후 카운트 결과를 리턴.

knight = list(input(">> "))
knight[1] = int(knight[1])
result = count_way(knight)
print(result)

