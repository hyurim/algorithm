# https://www.acmicpc.net/problem/11497
# 통나무 건너뛰기

caseNum = int(input()) # 테스트 케이스
for _ in range(caseNum):
	n = int(input()) # 통나무 개수
	height = list(map(int, input().split())) # 통나무 높이
	
	height.sort() # 오름 차순 정렬
	
	max_diff = 0 # 최대 높이
	# 양쪽에 번갈아 배치.
	# 두 칸 간격 차이 비교
	for i in range(2, n):
		max_diff = max(max_diff, abs(height[i] - height[i - 2]))
	
	# 나무 높이 최소차가 레벨과 동일함
	print(max_diff)