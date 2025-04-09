# https://www.acmicpc.net/problem/10799

stick = input()
stack = []

answer = 0

for i in range(len(stick)):
	if stick[i] == '(':
		stack.append('(')
	else:
		if stick[i-1] == '(':
			stack.pop()
			answer += len(stack)
		else:
			stack.pop()
			answer += 1
print(answer)