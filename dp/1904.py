import sys
	# 1.	작은 문제를 풀고
	# 2.	그걸 기반으로 점점 큰 문제를 만들고
	# 3.	중간 결과를 저장해서 재사용함
# 바텀업으로 해야하는 이유는 탑다운은 리커젼에 한계가 있기 때문
N = int(sys.stdin.readline())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[N])