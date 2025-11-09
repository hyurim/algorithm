# https://www.acmicpc.net/problem/2178
# 미로 탐색
# 최단 거리 구하는 것일 경우 - BFS

from collections import deque


N, M = map(int, input().split())
grid = [list(map(int, list(input()))) for _ in range(N)]

dist = [[0]*M for _ in range(N)] # 거리 배열
dist[0][0] = 1 # 시작칸 거리

q = deque([(0, 0)])
dirs = [(1,0), (-1,0), (0,1), (0,-1)]

while q:
	x, y = q.popleft()
	for dx, dy in dirs:
		nx, ny = x + dx, y + dy
		if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 1 and dist[nx][ny] == 0:
			dist[nx][ny] = dist[x][y] + 1
			q.append((nx, ny))
print(dist[N-1][M-1])
