i = 1

while True:
  q = int(input())
  if q == 0: break

  print('{0}. {1} {2}'.format(i, 'even' if q % 2 == 0 else 'odd', q // 2))
  i += 1