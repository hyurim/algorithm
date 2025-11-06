# https://school.programmers.co.kr/learn/courses/30/lessons/42578
# 의상
def solution(clothes):
    count = {}
    for name, kind in clothes: # 옷의 종류 개수
        if kind not in count: # count 해시에 kind가 없으면 0
            count[kind] = 0 # 예를 들면 모자, 안경 종류 등등
        count[kind] += 1 # 의상이 있을 경우 +1
        
    answer = 1 # 곱셈 누적용 초기 값
    for i in count.values():
        answer *= (i + 1) # 쓴다, 안쓴다의 경우라서 +1
    return answer - 1 # -1 하는 이유는 아무것도 안입는 경우를 제외하기 위해