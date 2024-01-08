import sys
read = sys.stdin.readline

ans = dict()
count = 0

while True:
  u = read().rstrip()
  if not u: break

  if ans.get(u):
    ans[u] += 1
  else:
    ans[u] = 1

  count += 1

for c in sorted(ans.keys()):
  r = ans.get(c) / count * 100
  print("%s %.4f" % (c, r))
