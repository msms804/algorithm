import sys

N, K = map(int, sys.stdin.readline().split())
coins = []
ret = 0
for i in range(N):
    coin = int(sys.stdin.readline())
    coins.append(coin)


coins.sort(reverse=True)

for coin in coins:
    # print(coin, "몫", K // coin)
    # print(coin, "나머지", K % coin)

    if K // coin > 0:
        ret += K // coin
        K = K % coin

print(ret)