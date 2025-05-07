# https://www.acmicpc.net/problem/14568
# 2017 연세대학교 프로그래밍 경시대회

num = int(input())

answer = 0 

for i in range(num):
	for j in range(num):
		for z in range(num):
			if i + j + z == num:
				if i >= j+2:
					if i != 0 and j != 0 and z != 0:
						if z % 2 == 0:
							answer += 1
print(answer)