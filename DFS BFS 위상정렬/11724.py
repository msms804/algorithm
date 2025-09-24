import sys

N, M = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
ret = 0

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

def dfs(u):
    visited[u] = 1
    for v in adj[u]:
        if visited[v] == 0:
            dfs(v)
    return

for i in range(1, N + 1):
    if visited[i] == 0:
        ret += 1
        dfs(i)

print(ret)
        