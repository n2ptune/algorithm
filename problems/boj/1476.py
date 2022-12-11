import sys

read = sys.stdin.readline

e, s, m = map(int, read().split(' '))
de, ds, dm = [1, 1, 1]


def trans_max():
  global de, ds, dm

  de += 1
  ds += 1
  dm += 1

  if de > 15:
    de = 1
  if ds > 28:
    ds = 1
  if dm > 19:
    dm = 1


ans = 1

while not [de, ds, dm] == [e, s, m]:
  trans_max()
  ans += 1

print(ans)