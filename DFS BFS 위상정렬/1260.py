import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# 정점 번호가 작은 것을 먼저 방문하도록 정렬
for g in graph:
    g.sort()

def dfs(x):
    visited_dfs[x] = True
    print(x, end=' ')
    for i in graph[x]:
        if(visited_dfs[i] == False):
            dfs(i)

def bfs(x):
    queue = deque([x])
    visited_bfs[x] = True
    while(queue):
        cur = queue.popleft()
        print(cur, end=' ')
        for i in graph[cur]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                queue.append(i)



dfs(V)
print()
bfs(V)