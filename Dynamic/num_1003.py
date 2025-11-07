# https://www.acmicpc.net/problem/1003
# 파보나치 함수

# 재귀로 했을 때 시간 초과가 발생함에 따라 점화식 사용
caseNum = int(input()) # 테스트 케이스 개수
num = [int(input()) for _ in range(caseNum)] # 계산할 정수
max_n = max(num) # 최대 정수만큼 미리 생성

# 0과 1 호출된 횟수 저장
dp0 = [0] * (max_n + 1)
dp1 = [0] * (max_n + 1)


dp0[0], dp1[0] = 1, 0 # fibonacci(0)

if max_n >= 1: 
	dp0[1], dp1[1] = 0, 1 # fibonacci(1)

for i in range(2, max_n + 1):
	dp0[i] = dp0[i - 1] + dp0[i - 2]
	dp1[i] = dp1[i - 1] + dp1[i - 2]

for n in num:
	print(dp0[n], dp1[n])
