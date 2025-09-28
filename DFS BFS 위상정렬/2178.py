import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

visited[0][0] = 1
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

queue = deque()
queue.append((0, 0))
while queue:
    y, x = queue.popleft()
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        # 언더플로 오버플로 검사해야
        if not (0 <= ny < N and 0 <= nx < M):
            continue
        if grid[ny][nx] == 0:
            continue
        if visited[ny][nx] != 0:
            continue

        visited[ny][nx] = visited[y][x] + 1
        queue.append((ny, nx))

print(visited[N - 1][M - 1])

