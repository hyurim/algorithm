# https://www.acmicpc.net/problem/1969

# A T G C 키 값으로 이루어진 리스트 하나 만들고

n, m = map(int, input().split())  # 첫 줄 정수 두 개 입력
data = [input() for _ in range(n)]  # n줄 동안 문자열 입력 받기

answer_text = ''
answer_num = 0

for i in range(m):
	dna = {'A' : 0, 'T' : 0, 'G' : 0, 'C' : 0}
	for j in range(n):
		dna[data[j][i]] += 1

			
	max_count = max(dna.values())
	select_dna = min([k for k, v in dna.items() if v == max_count])
	answer_text += select_dna

	for j in range(n):
		if data[j][i] != select_dna:
			answer_num += 1

print(answer_text)
print(answer_num)