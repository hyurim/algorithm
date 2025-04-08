# https://www.acmicpc.net/problem/10828
n = int(input())
commands = [input() for _ in range(n)]

stack = []

for i in commands:
	if i.startswith("push"):
		_, value = i.split()
		stack.append(int(value))
	elif i == 'pop':
		print(stack.pop() if stack else -1)
	elif i == 'size':
		print(len(stack))
	elif i == 'empty':
		print(0 if stack else 1)
	elif i == 'top':
		print(stack[-1] if stack else -1)