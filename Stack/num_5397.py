# https://www.acmicpc.net/problem/5397
# 5397.키로거

n = int(input())
passwords = [input() for _ in range(n)]  # n줄 입력 받기

for i in passwords:
	num = 0
	stack = []
	for j in i:
		if j == '<':
			if num > 0:
				num -= 1
		elif j == '>':
			if num < len(stack):
				num += 1
		elif j == '-':
			if num > 0:
				stack.pop(num - 1)
				num -= 1
		else:
			stack.insert(num, j)
			num += 1
	answer = ''.join(stack)
	print(answer)