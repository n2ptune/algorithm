import sys

read = sys.stdin.readline

for i in range(int(read())):
  r, c, e = map(int, read().split(' '))
  if c - e > r:
    print('advertise')
  elif c - e < r:
    print('do not advertise')
  else:
    print('does not matter')