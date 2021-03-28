# 실전 10-3. 커리큘럼: 선이수 과목이 존재할 때, N개의 강의 정보를 토대로 N개의 강의를 듣고자 한다면 수강하기까지 걸리는 최소 시간은?
import sys
from collections import deque

# 총 강의시간을 더해주는 함수
def how_long(i):
    # already: 해당 과목을 수강하기 위해 필요한 선이수 과목 목록 / order도 마찬가지이지만 겹칠 수도 있으므로 duplicates를 제거해준 목록이 already
    already = []
    result = time[i]
    order = deque()
    order += pre[i]
    # order queue가 비지 않았다면 (아직 선이수 과목을 더 고려해야한다면)
    while order:
        x = order.popleft()
        # 듣지 않은 과목이라면 already에 추가
        if x not in already:
            already.append(x)
        # 선이수과목의 선이수가 존재한다면 order에 추가
        order += pre[x]
        #print("order",order)
        #print("already",already)
    for j in already:
        result += time[j]
    return result

N = int(input(">> "))
pre = [[]]
time = list(range(N+1))

# 강의 시간, 선이수과목번호를 각각 time, pre에 저장 (pre에는 리스트가 저장됨)
for i in range(N):
    temp = list(map(int,sys.stdin.readline().split()))
    time[i+1] = temp[0]
    pre.append(temp[1:-1])

for i in range(1,N+1):
    print(how_long(i))