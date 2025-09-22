import sys

n = int(sys.stdin.readline())

triangle = []
dp = [[0] * n for _ in range(n)]
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    triangle.append(row)

dp[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(i + 1): # j는 0부터 i까지 포함해야
        if j == 0:
            dp[i][j] = dp[i - 1][j] + triangle[i][j]
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
        else:
            dp[i][j] = max(triangle[i][j] + dp[i - 1][j - 1], triangle[i][j] + dp[i - 1][j])

print(max(dp[n - 1]))