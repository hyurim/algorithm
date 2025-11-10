# https://www.acmicpc.net/problem/2579
# 계단 오르기
# 점화식을 유추하는 것이 중요

caseNum = int(input()) # 계단의 개수
num = [0] + [int(input()) for _ in range(caseNum)]

dp = [0] * (caseNum + 1)

if caseNum == 1:
	print(num[1])
else:
	dp[1] = num[1]
	dp[2] = num[1] + num[2]
	for i in range(3, caseNum + 1):
		dp[i] = max(dp[i - 2], dp[i - 3] + num[i - 1]) + num[i]
	print(dp[caseNum])