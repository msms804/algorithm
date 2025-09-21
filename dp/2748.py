import sys

n = int(sys.stdin.readline())
dp = [0] * 91

def fibo(x):
    if x == 0 or x == 1: return x
    if dp[x] != 0: return dp[x]
    dp[x] = fibo(x - 1) + fibo(x - 2)
    return dp[x]

print(fibo(n))