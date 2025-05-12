# https://www.acmicpc.net/problem/4673
# 셀프 넘버

numbers = set(range(1,10001))

gen = set(i + sum(map(int,str(i))) for i in range(1,10001))

nums = sorted(numbers - gen)

for i in nums:
	print(i)