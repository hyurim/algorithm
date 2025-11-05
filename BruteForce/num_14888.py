# https://www.acmicpc.net/problem/14888
# 연산자 끼워넣기

n = int(input()) # 수의 개수
num = list(map(int, input().split())) # 수
a, b, c, d = map(int, input().split()) # 사칙연산 개수
# a - 덧셈, b - 뺄셈, c - 곱셈, d - 나눗셈

min_num = 1000000000
max_num = -1000000000

def dfs(i, cur):
	global max_num, min_num, a, b, c, d

	if i == n:
		max_num = max(max_num, cur)
		min_num = min(min_num, cur)
		return
	
	if a:
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
	if d:
		d -= 1
		if cur < 0:
			dfs(i + 1, -(-cur // num[i]))
		else:
			dfs(i + 1, cur // num[i])
		d += 1

dfs(1, num[0])

print(max_num)
print(min_num)