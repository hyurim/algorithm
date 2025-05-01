# https://www.acmicpc.net/problem/17413
# 단어 뒤집기 2

text_input = input()

answer = []
text = []
check = False

for i in text_input:
    if i == '<':
        # 지금까지 쌓은 단어 뒤집어서 추가
        if text:
            text.reverse()
            answer.extend(text)
            text = []
        check = True
        answer.append(i)
    elif i == '>':
        check = False
        answer.append(i)
    elif check:
        answer.append(i)
    elif i == ' ':
        # 단어 끝났으면 뒤집어서 추가하고 공백 추가
        text.reverse()
        answer.extend(text)
        answer.append(' ')
        text = []
    else:
        text.append(i)

# 마지막 단어 처리
if text:
    text.reverse()
    answer.extend(text)

print(''.join(answer))