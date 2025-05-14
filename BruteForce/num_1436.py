# https://www.acmicpc.net/problem/1436
# 영화감독 숌

num = int(input())

devil_num = []
i = 1
while True:
	if len(devil_num) == num:
		break
	if '666'in str(i):
		devil_num.append(i)
	i += 1
	
print(devil_num[-1]) 