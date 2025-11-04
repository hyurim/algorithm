# https://www.acmicpc.net/problem/15903

# 카드 합체 놀이
import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split()) # 카드 개수, 카드 합체를 몇 번 하는지 나타내는 수
num = list(map(int, input().split())) # 맨 처음 카드 상태

heapq.heapify(num)

for _ in range(m):
	x = heapq.heappop(num) # 가장 작은 값
	y = heapq.heappop(num) # 두 번째로 작은 값
	s = x + y
	# 합친 값을 두 카드에 덮어 씌움.
	heapq.heappush(num, s) 
	heapq.heappush(num, s)
	
print(sum(num))