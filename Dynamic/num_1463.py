# https://www.acmicpc.net/problem/1463
# 1로 만들기

num = int(input()) # 숫자 입력값
dp = [0] * (num + 1) # 숫자를 1로 만드는 최소 연산 횟 수

for i in range(2, num +1):
	dp[i] = dp[i-1] + 1 # 우선 1을 빼는 경우를 기준으로 한 번 계산.
	if i % 2 == 0: # 2로 나누어질 때 1을 뺀 경우와 2로 나눈 경우 비교
		dp[i] = min(dp[i], dp[i//2] + 1)
	if i % 3 == 0: # 3로 나누어질 때 1을 뺀 경우와 3으로 나눈 경우 비교
		dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[num])