# https://www.acmicpc.net/problem/14888
# 연산자 끼워넣기

n = int(input()) # 수의 개수
num = list(map(int, input().split())) # 수
a, b, c, d = map(int, input().split()) # 사칙연산 개수
# a - 덧셈, b - 뺄셈, c - 곱셈, d - 나눗셈

min_num = 1000000000 # 가능한 최소 결과 값
max_num = -1000000000 # 가능한 최대 결과 값

def dfs(i, cur): # i - 현재까지 계산한 숫자의 인덱스 cur - 지금까지의 계산 결과
	global max_num, min_num, a, b, c, d 

	if i == n: # 모든 숫자를 다 사용했다면 현재 계산 결과를 최댓값과 최소값 갱신 후 종료
		max_num = max(max_num, cur)
		min_num = min(min_num, cur)
		return
	
	if a: # a가 1 이상이면 하나 줄이고 더한 결과로 dfs() 호출, 재귀 끝나면 원상 복구
		a -= 1
		dfs(i + 1, cur + num[i])
		a += 1
	if b:
		b -= 1
		dfs(i + 1, cur - num[i])
		b += 1
	if c:
		c -= 1
		dfs(i + 1, cur * num[i])
		c += 1
	if d: # // 연산은 음수를 내림을 하므로 0쪽으로 버리는 걸을 맞추기 위해 -(-cur // num[i])로 처리
		d -= 1
		if cur < 0:
			dfs(i + 1, -(-cur // num[i]))
		else:
			dfs(i + 1, cur // num[i])
		d += 1

dfs(1, num[0])

print(max_num)
print(min_num)