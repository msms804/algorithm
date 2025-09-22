import sys

n, k = map(int , sys.stdin.readline().split())
coins = []
dp = [0] * (k + 1)
dp[0] = 1 # 아무 동전도 쓰지 않는 1가지 방법
for _ in range(n):
    coin = int(sys.stdin.readline())
    coins.append(coin)

for coin in coins: # 1 2 5
    for i in range(coin, k + 1):# range(5, 11)
        dp[i] += dp[i - coin]

print(dp[k])