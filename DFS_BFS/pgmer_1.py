# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 타겟 넘버

# dfs 깊이 우선
def solution(numbers, target):
    answer = 0
    
    def dfs(idx, cur_sum):
        nonlocal answer
        
				# 모든 숫자 다 썼을 때 
        if idx == len(numbers):
						# 현재 값이 타겟 숫자와 같을 경우
            if cur_sum == target:
                answer += 1
            return
				# 재귀
        dfs(idx + 1, cur_sum + numbers[idx])
        dfs(idx + 1, cur_sum - numbers[idx])
    
    dfs(0, 0)
    return answer

# bfs 너비 우선
from collections import deque

def solution(numbers, target):
    queue = deque([(0, 0)]) # 현재 합, 인덱스
    answer_2 = 0
    
    while queue:
        current_sum, idx = queue.popleft()
        
				# 모든 숫자를 다 썼을 때
        if idx == len(numbers):
            if current_sum == target:
                answer_2 += 1
        else:
						# 현재 숫자에 +, -를 붙여 다음 단계로 이동
            queue.append((current_sum + numbers[idx], idx + 1))
            queue.append((current_sum - numbers[idx], idx + 1))
    return answer_2