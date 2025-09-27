
import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
parents = [0] * (N + 1)
visited = [False] * (N + 1)

for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

queue = deque([1])
visited[1] = True

while queue:
    node = queue.popleft()   
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            parents[neighbor] = node
            queue.append(neighbor)

for node in range(2, N + 1):
    print(parents[node])



