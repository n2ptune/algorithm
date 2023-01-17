N, M = map(int, input().split(' '))
ans = []
loc = [input().rstrip() for _ in range(N)]
w = ''
b = ''

for i in range(8):
  z = 'WBWBWBWB'

  if i % 2 == 0:
    w += z
  else:
    w += ''.join(list(reversed(z)))

for ch in w:
  b += 'W' if ch == 'B' else 'B'

for y in range(N - 7):
  for x in range(M - 7):
    a = ''.join(list(map(lambda z: z[x:x + 8], loc[y:y + 8])))
    ansb = []

    for t in [w, b]:
      z = 0
      for i, ch in enumerate(a):
        if not ch == t[i]:
          z += 1
      ansb.append(z)
      if z == 0:
        break

    ans.append(min(ansb))

print(min(ans))
