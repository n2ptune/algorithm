import sys
read = sys.stdin.readline

C, T = [int(read()) for _ in range(2)]
v = [0 for _ in range(C + 1)]
s = dict()

for _ in range(T):
  a, b = map(int, read().split(' '))
  
  if a in s: s[a].append(b)
  else: s[a] = [b]

  if b in s: s[b].append(a)
  else: s[b] = [a]


def sol(k):
  v[k] = 1
  if k in s:
    for i in s[k]:
      if v[i] == 0:
        sol(i)

  return sum(v) - 1


print(sol(1))