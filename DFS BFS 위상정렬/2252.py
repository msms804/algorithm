import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)


for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    indegree[B] += 1

q = deque([i for i in range(1, N + 1) if indegree[i] == 0])
result = []

while q:
    cur = q.popleft()
    result.append(cur)

    for nxt in graph[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)
        
# *: 언패킹 연산자, 리스트나 튜플같은 iterable을 풀어서 각각의 원소로 꺼내주는 역할
print(*result)