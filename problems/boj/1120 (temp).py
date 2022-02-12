import sys

read = sys.stdin.readline

X, Y = read().rstrip().split(' ')


def diff(a, b):
  r = 0
  for i in range(len(a)):
    if a[i] != b[i]:
      r += 1
  return r


if len(X) == len(Y):
  ans = diff(X, Y)
  print(ans)
else:
  d = 0
  for j in range(len(X)):
    s = X[j:]
    if s in Y:
      break
    d += 1
  print(d)