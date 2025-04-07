# https://www.acmicpc.net/problem/19941

# 1. 왼쪽을 먼저 생각하고 없을 경우 오른쪽

n, k = list(map(int, input().split()))
table = list(input())

answer = 0

for i in range(n):
  if table[i] == 'P':
    for j in range(i-k, i+k+1):
      if 0 <= j < n and table[j] == "H":
        answer += 1
        table[j] = "E"
        break
print(answer)
