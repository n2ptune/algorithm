import sys
n, *a = map(int, sys.stdin.buffer.read().splitlines())
d = dict()
a = list(sorted(a))
res = []

res.append(round(sum(a) / n))
res.append(a[int(len(a) / 2)])

for b in a:
  if b in d:
    d[b] += 1
  else:
    d[b] = 1

mv = max(d.values())
t = sorted(list(set([key for key, value in d.items() if value == mv])))

if len(t) > 1:
  res.append(t[1])
else:
  res.append(t[0])

res.append(a[-1] - a[0])

print('\n'.join(map(str, res)))