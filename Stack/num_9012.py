# https://www.acmicpc.net/problem/9012

n = int(input())        # 첫 줄: 테스트 케이스 수
cases = [input() for _ in range(n)]  # n줄 입력 받기


for i in cases:
  stack = []

  if len(i) % 2 == 1:
    print('NO')
    continue
  
  for j in i:
    if j == '(':
      stack.append(j)
    elif j == ')':
      if stack:
        stack.pop()
      else:
        print('NO')
        break
  else:
    print('YES' if not stack else 'NO')