# 무지의 먹방 라이브 짧은 코드 도전!
import numpy as np
def solution(f_,k):
    f = np.array(f_)
    f -= 1
    print(f)
    print(f[7])
    answer = 0
    count(i for i in f if i > 0)
    return answer

f = [3,1,2,2,1,1,1,4,3]
k = 10
if solution(f,k) == 3:
    print("correct")
else:
    print("fail")