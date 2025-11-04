# https://www.acmicpc.net/problem/1260
# DFS와 BFS

from collections import deque

n, m, v = list(map(int, input().split())) # 정점의 개수, 간선의 개수, 탐색을 시작항 정점의 번호
graph = [[] for _ in range(n + 1)]  # 간선이 연결하는 두 정점의 번호

# 간선 입력 받기
for _ in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

# 각 노드의 인접 리스트 정렬 (번호 작은 순)
for i in range(1, n+1):
	graph[i].sort()

# DFS 구현 (재귀)
def dfs(v, visited):
    visited[v] = True
    print(v, end=' ')
    for nxt in graph[v]:
        if not visited[nxt]:
            dfs(nxt, visited)

# BFS (deque)
def bfs(start):
    visited = [False] * (n + 1)
    queue = deque([start])  # 시작 노드를 큐에 넣기
    visited[start] = True

    while queue:
        cur = queue.popleft()  # 큐에서 가장 앞의 원소 꺼냄
        print(cur, end=' ')
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

# 실행
visited = [False] * (n + 1)
dfs(v, visited)
print()
bfs(v)