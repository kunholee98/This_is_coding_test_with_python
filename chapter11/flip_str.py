# 3. 문자열 뒤집기: 0과 1로만 된 문자열을 받아서 전체 혹은 일부 구간을 뒤집어(0은 1로, 1은 0으로) 모두 같은 숫자로 만들기 위해 필요한 뒤집는 횟수는?
import sys

s = sys.stdin.readline().strip()
pre = s[0]
standard = s[0]
cnt = 0
for i in range(len(s)):
    j = s[i]
    if j != pre:
        pre = j
        if j != standard:
            cnt +=1
print(cnt)
        
