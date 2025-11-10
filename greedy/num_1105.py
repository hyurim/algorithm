# https://www.acmicpc.net/problem/1105
# 팔
import sys

input = sys.stdin.readline # 입력 속도 향상

l, r = input().split() # 왼, 오

if len(l) != len(r): # 자리 수가 다르면 무조건 0, 8이 하나도 없는 숫자를 항상 고를 수 있음.
	print(0)
else:
	count = 0
	for n, m in zip(l, r): # 왼쪽 자리부터 차례대로 비교
		if n != m: #
			break
		if n == '8': # 같은 자리 숫자가 둘 다 8이면 그 자리는 무조건 8
			count += 1
	print(count)