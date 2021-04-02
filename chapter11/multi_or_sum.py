# 2. 곱하기 혹은 더하기: 일련의 수를 입력받으면 좌측부터 우측 순으로 각 숫자를 더하거나 곱한다. (모든 연산은 좌측에서부터) 이때 최댓값은?
import sys

s = str(sys.stdin.readline().strip())
result = 0
print(s)
for i in range(len(s)):
    #n = int(s[i])
    print(n)
    if n == 0 or n == 1 or result == 0 or result ==1 :
        result += n
    else:
        result *= n
print(result)