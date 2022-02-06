import sys

read = sys.stdin.readline

while True:
  N = int(read())
  if N == 0:
    break

  cases = []

  for _ in range(N):
    p, h = read().rstrip().split(' ')
    cases.append((p, float(h)))

  max_height = max(map(lambda x: x[1], cases))
  max_height_case = list(filter(lambda x: x[1] == max_height, cases))

  print(' '.join(map(lambda x: x[0], max_height_case)))