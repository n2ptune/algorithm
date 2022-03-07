for _ in range(int(input())):
  a = [input() for __ in range(2)]
  d = 0
  for i in range(len(a[0])):
    if a[0][i] != a[1][i]:
      d += 1
  print('Hamming distance is {0}.'.format(d))
