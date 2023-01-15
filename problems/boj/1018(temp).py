import sys
from pprint import pp

read = sys.stdin.readline

N, M = map(int, read().split(' '))
ans = []
loc = [read().rstrip() for _ in range(N)]
w = []
b = []

for i in range(8):
  z = 'WBWBWBWB'

  if i % 2 == 0:
    w.append(z)
  else:
    w.append(''.join(list(reversed(z))))

b = list(map(lambda x: ''.join(x), map(list, map(reversed, w))))

for y in range(N - 8):
  for x in range(M - 8):
    a = list(map(lambda z: z[x:x + 8], loc[y:y + 8]))

    for p in [w, b]:
      ansb = 0
      for i, t in enumerate(a):
        if t == p[i]:
          continue
        else:
          for j, u in enumerate(t):
            if not u == p[i][j]:
              ansb += 1
      ans.append(ansb)

print(min(ans))

# ans1 = 0
# ans2 = 0

# loc = [list(read().rstrip()) for _ in range(N)]
# start = loc[0][0]
# even = []
# odd = []

# for i in range(M):
#   if i % 2 == 0:
#     even.append('W' if start == 'W' else 'B')
#     odd.append('B' if start == 'W' else 'W')
#   else:
#     even.append('B' if start == 'W' else 'W')
#     odd.append('W' if start == 'W' else 'B')

# for y in range(0, N):
#   for x in range(0, M):
#     current = loc[y][x]

#     if y % 2 == 0 and not current == even[x]:
#       ans1 += 1
#     elif not y % 2 == 0 and not current == odd[x]:
#       ans1 += 1

# temp = even
# even = odd
# odd = temp

# for y in range(0, N):
#   for x in range(0, M):
#     current = loc[y][x]

#     if y % 2 == 0 and not current == even[x]:
#       ans2 += 1
#     elif not y % 2 == 0 and not current == odd[x]:
#       ans2 += 1

# print(ans1, ans2, even, odd)
