import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
dist = [-1] * (N + 1) # -1은 방문하지 않은 노드

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)

q = deque()
q.append(X)
dist[X] = 0

while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        if dist[nxt] == -1:
            dist[nxt] = dist[cur] + 1
            q.append(nxt)

ret = []
for i in range(N + 1):
    if dist[i] == K:
        ret.append(i)

if ret:
    ret.sort()
    for node in ret:
        print(node)
else:
    print(-1)