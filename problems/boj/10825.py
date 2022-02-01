import sys

read = sys.stdin.readline

N = int(read())
ans = []

for _ in range(N):
  [name, k, e, m] = map(str, read().rstrip().split(' '))
  ans.append([name, int(k), int(e), int(m)])

sor = sorted(ans, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for s in sor:
  print(s[0])