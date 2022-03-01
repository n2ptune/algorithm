import sys

read = sys.stdin.readline

while True:
  line = read().rstrip()

  if line == '*':
    break

  chrs = [chr(i) for i in range(97, 123)]
  x = {}

  for ch in chrs:
    x[ch] = 0

  for l in line:
    if l == ' ':
      continue
    x[l] += 1

  ans = len(list(filter(lambda x: x[1] == 0, x.items())))
  print('Y' if ans == 0 else 'N')