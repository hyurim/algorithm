day = int(input()) # 전체 근무 일수
t = []
p = []

for _ in range(day):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

dp = [0] * (day + 2) # 배열 초기화, dp[i]는 i번째 날부터 퇴사일까지 얻을 수 있는 최대 수익
# day +2로 만드는 이유: day+1일은 퇴사 다음 날(상담 불가)를 표시하기 위해.

for i in range(day, 0, -1): # 역순으로 반복
	# 미래의 결과(dp[i + t[i-1]], dp[i+1])를 먼저 계산해놔야 현재 선택의 결과를 알 수 있기 때문
    if i + t[i-1] <= day + 1: # i번째 날에 시작한 상담이 퇴사 전에 끝나는지 확인.
        dp[i] = max(p[i-1] + dp[i + t[i-1]], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[1])