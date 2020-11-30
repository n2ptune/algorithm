S = list(map(int, list(input())))


def calTwoNum(a, b):
  if a == 0 or b == 0:
    return a + b
  elif a == 1 or b == 1:
    return a + b
  else:
    return a * b


if len(S) == 1:
  print(S[0])
elif len(S) == 2:
  print(calTwoNum(S[0], S[1]))
else:
  C = calTwoNum(S[0], S[1])
  S = S[2:]

  for num in S:
    C = calTwoNum(C, num)

  print(C)