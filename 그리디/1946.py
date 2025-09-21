import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    grades = []
    ret = 1
    for j in range(N):
        grade1, grade2 = map(int, sys.stdin.readline().split())
        grades.append((grade1, grade2))
    
    grades.sort(key=lambda x: (x[0]))

    tmp = grades[0][1]
    for grade in grades:
        if grade[1] < tmp:
            ret += 1
            tmp = grade[1]
    print(ret)