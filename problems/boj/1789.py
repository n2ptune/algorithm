import sys

read = sys.stdin.readline

ans = 0
c = 0
S = int(read())

for i in range(0, S):
  ans += (i + 1)
  c += 1
  if ans > S:
    c -= 1
    break
print(c)