a, b = input().split(' ')

def diffCnt(l, r):
  cnt = 0
  for i, ch in enumerate(l):
    if not ch == r[i]:
      cnt += 1
  return cnt

if len(a) == len(b):
  print(diffCnt(a, b))
else:
  try:
    c = b.index(a)
    print(0)
  except:
    