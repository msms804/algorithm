import sys
from collections import deque

K = int(sys.stdin.readline())

for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V + 1)]
    color = [-1] * (V + 1)

    for i in range(E):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    queue = deque()
    is_bipartite = True

    for start in range(1, V + 1):
        if color[start] != -1:
            continue
        queue.append(start)
        color[start] = 0

        while queue and is_bipartite:
            cur = queue.popleft()
            for nxt in graph[cur]:
                if color[nxt] == -1:
                    color[nxt] = 1 - color[cur]
                    queue.append(nxt)
                elif color[nxt] == color[cur]:
                    is_bipartite = False
                    break
        
        if not is_bipartite:
            break

    if is_bipartite:
        print("YES")
    else:
        print("NO")
