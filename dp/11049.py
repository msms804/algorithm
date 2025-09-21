import sys

N = int(sys.stdin.readline()) # 행렬의 개수
matrix = []
INF = 2 ** 31 - 1
dp = [[INF] * N for _ in range(N)]
# dp[i][j] -> i ~ j 행렬까지의 최소 연산 횟수
for i in range(N):
    r, c = map(int, sys.stdin.readline().split())
    matrix.append((r, c))
    dp[i][i] = 0 # 자기 자신 하나만 곱할 땐 연산 0번

# length : 몇개의 행렬 곱할지 i : 시작하는 행렬번호 j : 끝나는 행렬번호 / k : (i~j)를 둘로 나누는 분할점 = 괄호 위치 결정자
for length in range(2, N+1): 
    for i in range(N - length + 1): # 시작점
        j = i + length - 1 # 끝점
        for k in range(i, j): # 괄호의 위치
            cost = matrix[i][0] * matrix[k][1] * matrix[j][1]
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + cost)

print(dp[0][N - 1])
