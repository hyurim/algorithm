# https://www.acmicpc.net/problem/2503
# 숫자 야구

num = int(input())

ans = [list(map(int, input().split())) for _ in range(num)]

answer = 0 
for i in range(1,10):
	for j in range(10):
		for k in range(10):
			if (i == j or j == k or k == i):
				continue
			cnt = 0
			for arr in ans:
				number, strike, ball = arr
				number = list(map(int,str(number)))	
				ball_count = 0
				strike_count = 0

				guess = [i, j, k]

				for x in range(3):
					if guess[x] == number[x]:
						strike_count += 1
					elif guess[x] in number:
						ball_count += 1

				if ball == ball_count and strike == strike_count:
					cnt += 1
			if cnt == num:
				answer += 1
print(answer)