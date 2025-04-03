# 5로 나눈 값 V
# 최소한의 3과 최대한의 5 V
# 3으로 나눈 값 V
# 안담아지는거 V

num = int(input())

if num % 5 == 0: # 5로 나눈 값
  print(num // 5)
else:
  i = 0 # 봉투
  while num > 0:
    num -= 3
    i += 1

    if num % 5 == 0: # 최소한의 3과 최대한의 5 V
      i += num // 5
      print(i)
      break
    
    if num == 0: # 3으로 나눈 값 V
      i += num // 3
      print(i)
      break

    if num == 1 or num == 2: # 안담아지는거 V
      print(-1)
      break
