# https://www.acmicpc.net/problem/11726
# 2xn 타일링

num = int(input()) # 정수 입력값
dp = [0] * (num + 2) # 인덱스 에러 방지

# 초기값
dp[1] = 1
dp[2] = 2

# 파보나치랑 비슷함.
for i in range(3, num + 1):
	dp[i] = (dp[i-1] + dp[i-2]) % 10007

# 출력
print(dp[num])