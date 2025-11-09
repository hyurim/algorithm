# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 게임 맵 최단거리

from collections import deque

def solution(maps):
    n = len(maps) # 행 개수
    m = len(maps[0]) # 열 개수
    
    dist = [[0]*m for _ in range(n)] # 거리 배열
    dist[0][0] = 1 # 시작칸 거리
    
    q = deque([(0, 0)])
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    while q:
        x, y = q.popleft()
        if x == n-1 and y == m-1:
            return dist[x][y]
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and dist[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    return -1