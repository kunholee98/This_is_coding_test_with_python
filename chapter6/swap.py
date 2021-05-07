#연습

'''n = int(input())
students = []
for _ in range(n):
    student = list(map(str, input().split()))
    students.append((student[0], int(student[1])))
students.sort(key=lambda student: student[1])

for student in students:
    print(student[0], end= ' ')'''

n,k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
for i in range(k):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break
print(A)
print(B)
print(sum(A))
