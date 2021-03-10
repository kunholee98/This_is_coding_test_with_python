# 실전 4-2. 성적이 낮은 순서로 학생 출력하기: N명의 학생 정보(이름과 성적으로 구성)가 주어졌을 때, 성적이 낮은 순으로 학생의 이름을 출력하라.
def setting(key):
    return key[1]
N = int(input(">> "))
student = []
for i in range(N):
    student.append(input(">> ").split())
    student[i][1] = int(student[i][1])
result = sorted(student, key=setting)
print(' '.join(result[i][0] for i in range(N)))