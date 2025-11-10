# https://www.acmicpc.net/problem/1149
# RGB 거리

# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다


house = int(input()) # 집의 수
cost = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(house)] # 각각 R, G, B로 칠하는 비용

dp = [[0, 0, 0] for _ in range(house + 1)] # i 번째 집까지 칠했을 때, i번 째 집의 색이 (0=R,1=G,2=B)일 때의 최소 비용
dp[1] = cost[1][:] # 첫 번째 집은 이전 집이 없으므로, 단순히 해당 색의 비용이 최소 값이다.

# 각 집은 이전 집과 같은 색을 가질 수 없음.
for i in range(2, house + 1):

	# i번 째 집이 빨간색 일 경우 - 이전 집은 G or B
	dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2]) 
    # i번 째 집이 초록색 일 경우 - 이전 집은 R or B
	dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2]) 
    # i번 째 집이 파란색 일 경우 - 이전 집은 R or G
	dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1]) 

print(min(dp[house]))