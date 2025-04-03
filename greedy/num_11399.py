# https://www.acmicpc.net/problem/11399

peo = int(input())
data = list(map(int, input().split()))

min = 0
answer = 0

data.sort()

for i in data:
  min += i
  answer += min
  
print(answer)