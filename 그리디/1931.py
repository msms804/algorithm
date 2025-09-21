import sys

N = int(sys.stdin.readline())
rooms = []
# 최대한 많은 회의갯수를 구하려면 endTime이 빨라야함

for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    rooms.append((start, end))

# endTime 기준으로 오름차순 정렬
# ✅ 끝나는 시간 오름차순, 시작 시간 오름차순 (동 tie-breaker)
rooms.sort(key=lambda x: (x[1], x[0]))

ret = 0
currentEndTime = 0

for i in range(N):
    if currentEndTime <= rooms[i][0]:
        currentEndTime = rooms[i][1]
        ret += 1

print(ret)