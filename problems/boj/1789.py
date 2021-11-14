import sys
read = sys.stdin.readline

n = 0
c = 0
S = int(read())

for i in range(1, S):
  n += i
  c += 1
  if n > S:
    c -= 1
    break

print(c)