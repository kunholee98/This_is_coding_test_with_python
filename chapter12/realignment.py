# 8. 문자열 재정렬
# 모든 문자는 오름차순으로 정렬하고, 숫자는 모두 더하여 문자열에 이어서 출력

string = list(map(str, input()))
print(string)
char = []
num = []
for i in string:
    if i.isalpha():
        char.append(i)
    else:
        num.append(int(i))
char.sort()
sum_num = str(sum(num))
print(''.join(char)+sum_num)
