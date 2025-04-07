# https://www.acmicpc.net/problem/1026

num = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = 0

a.sort()
b.sort(reverse=True)

for i in range(num):
  answer += a[i] * b[i]
print(answer)