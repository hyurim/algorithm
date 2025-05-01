from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
dq = deque()

for _ in range(n):
	command = input().strip()

	if command.startswith("push_back"):
		_, x = command.split()
		dq.append(int(x))
	elif command.startswith("push_front"):
		_, x = command.split()
		dq.appendleft(int(x))
	elif command == "pop_front":
		print(dq.popleft() if dq else -1)
	elif command == "pop_back":
		print(dq.pop() if dq else -1)
	elif command == "size":
		print(len(dq))
	elif command == "empty":
		print(0 if dq else 1)
	elif command == "front":
		print(dq[0] if dq else -1)
	elif command == "back":
		print(dq[-1] if dq else -1)
			