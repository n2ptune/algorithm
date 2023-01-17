while True:
  a, b, c = map(int, input().split(' '))

  if a == 0 and b == 0 and c == 0:
    break

  ma = max([a, b, c])
  mi = min([a, b, c])
  mid = list(filter(lambda x: not x == ma and not x == mi, [a, b, c]))[0]

  print('right' if (mi**2) + (mid**2) == ma**2 else 'wrong')
