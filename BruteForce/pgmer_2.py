# https://school.programmers.co.kr/learn/courses/30/lessons/42840
# 모의고사

def solution(answers):
    student = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    scores = []
    for i in student:
        count = 0
        for j in range(len(answers)):
            if answer[j] == i[j % len(i)]:
                count += 1
        scores.append(count)
        
    max_score = max(scores)
    answer = [i + 1 for i, s in enumerate(scores) if s == max_score]
    
    return answer