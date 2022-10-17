while True:
  a = int(input())
  if a == -1:
    break
  n = []
  for i in range(1, int(a / 2) + 1):
    if a % i == 0:
      n.append(i)
  if sum(n) == a:
    print('{0} = {1}'.format(a, ' + '.join(list(map(str, n)))))
  else:
    print('{0} is NOT perfect.'.format(a))