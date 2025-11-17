# https://www.acmicpc.net/problem/11053
# 가장 긴 증가하는 부분 수열

n = int(input()) # 수열의 크기
arr = list(map(int, input().split())) # 수열 입력

dp = [1] * n # 수열 최대 길이 (자기 자신만 포함한 길이)

for i in range(1, n): # 2번째부터 마지막까지 (첫 번째는 자기 자신이라 제외) 
	for j in range(i): # i 이전의 모든 원소와 비교함.
		if arr[i] > arr[j]: # i값이 j값보다 크면 수열이 증가한다는 의미
			dp[i] = max(dp[i], dp[j] + 1) # dp[i] 값 갱신
print(max(dp))

