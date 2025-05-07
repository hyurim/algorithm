# https://www.acmicpc.net/problem/19532
# 수학은 비대면강의입니다

A,B,C,D,E,F = map(int, input().split())

for x in range(-1000, 1001):
	for y in range(-1000, 1001):
		if A * x + B * y == C and D * x + E * y == F:
			print(f"{x} {y}")
			break
		