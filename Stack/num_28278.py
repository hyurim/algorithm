# https://www.acmicpc.net/problem/28278
# 스택 2

import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    line = input().strip()
    command = list(map(int, line.split()))
    arr.append(command)

answer_arr = []

for i in arr:
	if i[0] == 1:
		answer_arr.append(i[1])
	elif i[0] == 2:
		print(answer_arr.pop() if answer_arr else -1)
	elif i[0] == 3:
		print(len(answer_arr))
	elif i[0] == 4:
		print(0 if answer_arr else 1)
	elif i[0] == 5:
		print(answer_arr[-1] if answer_arr else -1)