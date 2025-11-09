# https://www.acmicpc.net/problem/2606
# 바이러스
# 1번 컴퓨터가 웜 바이러스에 걸렸을 때 같이 걸리는 컴퓨터의 수

n = int(input()) # 컴퓨터의 수
m = int(input()) # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

graph = [[] for _ in range(n + 1)]  # 연결 되어 있는 컴퓨터(인접 리스트)

# 컴퓨터 입력 받기
for _ in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

visited = [False]*(n+1) # 각 노드가 방문했는지 표시하는 리스트
# 0번 인덱스는 사용하지 않으므로 n+1 크기로 생성
# 초기에는 아무도 방문하지 않으므로 모두 False

# --------------------

# 재귀
def dfs(v):
	visited[v] = True # v번 노드 방문 표시
	for nv in graph[v]: 
		if not visited[nv]: # 연결된 컴퓨터 nv 노드가 아직 방문되지 않았다면 재귀
			dfs(nv)

dfs(1) 
print(sum(visited) - 1) # 1번 컴퓨터를 통해서 걸린 다른 컴퓨터만 세야하므로 -1

# --------------------

# 스택
stack = [1] # 다음에 방문할 리스트
visited[1] = True # 감염이 시작됐으므로 체크

while stack: # 방문할 노드가 남아있는 동안 계속 반복
	v = stack.pop() # 지금 방문 중인 컴퓨터 번호
	for nv in graph[v]: # v와 연결된 컴퓨터 확인
		if not visited[nv]: # 방문하지 않은 컴퓨터 일 경우
			visited[nv] = True # 방문 표시
			stack.append(nv) # 다음에 탐색할 노드로 등록

print(sum(visited) - 1) #  1번 컴퓨터를 통해서 걸린 다른 컴퓨터만 세야하므로 -1