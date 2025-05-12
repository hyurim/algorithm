# https://www.acmicpc.net/problem/1065
# 한수

num = int(input())

answer = 0

for i in range(1, num+1):
	if i < 100:
		answer += 1
	else:
		number = list(map(int,str(i)))
		diff = number[1] - number[0]
		for j in range(1, len(number) - 1):
			if number[j+1] - number[j] != diff:
				break
		else:
			answer += 1
print(answer)
