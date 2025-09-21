import sys
# 0-1 배낭문제
N, K = map(int, sys.stdin.readline().split()) # 물건 개수, 최대 무게
bag = []
# dp[i]는 “총 무게가 정확히 i일 때 만들 수 있는 최대 가치”를 의미
dp = [[0] * (K + 1) for _ in range(N + 1)]
# hint: dp는 2차원 배열
# 뭔가 LCS랑 비슷한거같
for i in range(N):
    W, V = map(int, sys.stdin.readline().split()) # 무게, 가치
    bag.append((W, V))


for i in range(1, N + 1):
    weight = bag[i - 1][0]
    value = bag[i - 1][1]

    for j in range(K + 1):
        if j < weight:
            dp[i][j] = dp[i - 1][j] # 현재 물건 못 넣음
        else: # 넣는 경우 vs 안 넣는 경우 중 큰 값 선택
            dp[i][j] = max(dp[i - 1][j], value + dp[i - 1][j - weight])

print(dp[N][K])



# 4 7
# 6 13
# 4 8
# 3 6
# 5 12