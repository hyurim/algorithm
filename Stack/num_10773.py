# https://www.acmicpc.net/problem/10773

n = int(input())
money = [int(input()) for _ in range(n)]  # n줄 입력 받기

stack = []
answer = 0

for i in money:
	if i == 0:
		minus = stack.pop()
		answer -= minus
	else:
		add = stack.append(i)
		answer += i

print(answer)