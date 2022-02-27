import sys

read = sys.stdin.readline

T, K = read().rstrip().split(' ')
ans = []

if len(T) == 1:
  ans += list(range(1, int(T) + 1))
else:
  ans += list(range(1, 10))
  l = len(T)

  if l > 2:
    for i in range(2, l):
      a, b = [(10**(i - 1)), 10**i]
      # ans += len(range(a, b)) * i
      ans += list(range(a, b))

  m = 10**(l - 1)
  # ans += ((int(T) - m) + 1) * l
  ans += list(range(m, int(T) + 1))

ans = ''.join(map(str, ans))

try:
  ansb = ans[int(K) - 1]
  print(ansb)
except:
  print(-1)