import sys
from pprint import pp

read = sys.stdin.readline

N, M = map(int, read().split(' '))
ans = 0

loc = [list(read().rstrip()) for _ in range(N)]

for y in range(0, N):
  for x in range(0, M):
    current = loc[y][x]

    fr, fb = [0, 0]
    tr, tb = [0, 0]

    if M - 1 == x and N - 1 == y:
      fr = x - 1
      fb = y
      tr = x
      tb = y - 1
    elif M - 1 == x:
      fr = x - 1
      fb = y
      tr = x
      tb = y + 1
    elif N - 1 == y:
      fr = x + 1
      fb = y
      tr = x
      tb = y - 1
    else:
      fr = x + 1
      fb = y
      tr = x
      tb = y + 1

    # Check
    v = loc[fb][fr]
    h = loc[tb][tr]

    if current == v and current == h:
      loc[y][x] = 'W' if current == 'B' else 'B'
      ans += 1
      print(v, h, current, current == v and current == h, y, x, fr, fb, tr, tb)

print(ans)
pp(loc)