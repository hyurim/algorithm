# https://www.acmicpc.net/problem/1080
# 행렬

n, m = map(int, input().split()) # 행렬 크기
a = [list(map(int, list(input().strip()))) for _ in range(n)]
b = [list(map(int, list(input().strip()))) for _ in range(n)]

# 문제에서 설명하는 3x3 크기 뒤집기
def flip(x, y): 
    for i in range(x, x+3):
        for j in range(y, y+3):
            a[i][j] = 1 - a[i][j] 


cnt = 0 # 뒤집기 횟 수

for i in range(n - 2): # 뒤집기 가능한 행
    for j in range(m - 2): # 뒤집가 가능한 열
        if a[i][j] != b[i][j]: # 두 행렬 원소가 다르면 뒤집기
            flip(i, j) # 해당 위치 기준으로 뒤집기
            cnt += 1 # 뒤집은 횟 수 +1

print(cnt if a == b else -1) # 두 행렬이 같으면 뒤집은 횟수 or 같게 만들 수 없으면 -1