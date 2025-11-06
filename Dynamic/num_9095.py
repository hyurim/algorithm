# https://www.acmicpc.net/problem/9095
# 1, 2, 3 더하기

caseNum = int(input()) # 테스트 케이스 개수
num = [int(input()) for _ in range(caseNum)] # 계산할 정수
max_n = max(num) # 입력된 수 중 가장 큰 값 (DP를 여기까지만 계산) 즉, 5, 7, 10을 입력받으면 10까지 계산함.

dp = [0] * (max_n + 1) # dp[i] = i를 1, 2, 3의 합으로 나타내는 방법의 수

# 초기 값 설정 (3 이상이라면 if문 필요 X)
dp[1] = 1 # 1의 합을 나타내는 수
if max_n >= 2: # 입력된 최대값이 2 이상일 때만 계산
    dp[2] = 2
if max_n >= 3: # 입력된 최대값이 3 이상일 때만 계산
    dp[3] = 4 

for i in range(4, max_n + 1):
	# 마지막에 1을 더한 경우(dp[i-1]), 2를 더한 경우(dp[i-2]), 3을 더한 경우(dp[i-3])의 합
	dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for j in num: 
	print(dp[j])