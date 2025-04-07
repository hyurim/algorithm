# https://www.acmicpc.net/problem/10610

num = list(map(int, input()))

num.sort(reverse=True)
answer = int(''.join(map(str, num)))

print(answer) if answer % 30 == 0 else print(-1)
