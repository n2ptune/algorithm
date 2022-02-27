import sys
read = sys.stdin.readline


def gcd(a, b):
  r = 0
  while not b == 0:
    r = a % b
    a = b
    b = r
  return a


for i in range(int(read())):
  n = list(map(int, read().split(' ')))[1:]
  gcds = []
  for k, t in enumerate(n):
    if len(n) - 1 <= k:
      break
    else:
      for m in n[k + 1:]:
        gcds.append(gcd(t, m))
  print(sum(gcds))