import sys
read = sys.stdin.readline

N = int(read())
an = list(map(int, read().split(' ')))
M = int(read())
am = list(map(int, read().split(' ')))
t = {}
s = [0 for _ in range(M)]

for i, v in enumerate(am):
  if not t.get(v):
    t[v] = [i]
  else:
    t[v].append(i)

for k in an:
  if k in t.keys():
    v = t.get(k)
    for o in v:
      s[o] += 1

print(' '.join(list(map(str, s))))