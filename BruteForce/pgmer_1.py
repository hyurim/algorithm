# https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 피로도 (완전탐색)

def solution(k, dungeons):
    n = len(dungeons)
    used = [False] * n
    answer = 0

    def dfs(current_fatigue, cleared):
        nonlocal answer
        if cleared > answer:
            answer = cleared

        for i in range(n):
            req, cost = dungeons[i]
            if not used[i] and current_fatigue >= req:
                used[i] = True
                dfs(current_fatigue - cost, cleared + 1)
                used[i] = False
    dfs(k,0)
    return answer
