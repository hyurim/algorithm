day = int(input())
t = []
p = []

for _ in range(day):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

max_money = 0
first_day = 1

for i in range(1, day+1):
	1