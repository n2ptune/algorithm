import sys

read = sys.stdin.readline

T = read().rstrip()
ans = 0

if len(T) == 1:
  ans = int(T)
else:
  ans += len(range(1, 10))

  l = len(T)
  m = 10**(l - 1)
  ans += ((int(T) - m) + 1) * l

  if l > 2:
    for i in range(l - 1, 1, -1):
      a, b = [(10**(i - 1)), 10**i]
      ans += len(range(a, b)) * i

print(ans)