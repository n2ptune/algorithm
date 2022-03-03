import sys

read = sys.stdin.readline

T = int(read())
ha = {}

for _ in range(T):
  s = int(read())

  if not ha.get(s):
    ha[s] = 1
  else:
    ha[s] += 1

ans = sorted(ha.items(), key=lambda x: (-x[1], x[0]))
print(ans[0][0])