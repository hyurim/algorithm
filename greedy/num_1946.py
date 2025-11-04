#https://www.acmicpc.net/problem/1946

#

import sys
input = sys.stdin.readline

n = int(input()) # 테스트 케이스의 개수
for _ in range(n):
	m = int(input()) # 지원자의 숫자
	people = []
	for _ in range(m):
		a, b = map(int, input().split())
		people.append((a, b))

	people.sort() # 서류 오름차순

	count = 0
	best = 100001 # 최대 등수

	for doc, interview in people:
		if interview < best:
			count += 1
			best = interview
	print(count)
