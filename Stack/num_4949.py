# https://www.acmicpc.net/problem/4949

def text_isVaild(text):
	stack = []
	
	for j in text:
		if j == '(' or j == '[':
			stack.append(j)
		elif j == ')':
			if not stack or stack[-1] != '(':
				return False
			stack.pop()
		elif j == ']':
			if not stack or stack[-1] != '[':
				return False
			stack.pop()
	return not stack # stack이 비어있으면 True

texts = []
while True:
    line = input()
    if line == ".":
        break
    texts.append(line)
# 입력 텍스트

for i in texts:
	print('yes' if text_isVaild(i) else 'no')