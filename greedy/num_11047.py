# https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())  # n: 동전 종류 수, k: 목표 금액

coins = []
for _ in range(n):
    coins.append(int(input()))

answer = 0 
coins.reverse()

for i in coins:
  if k // i != 0:
    answer += k // i
    k %= i
    
print(answer)