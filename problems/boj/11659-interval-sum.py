import sys
read = sys.stdin.readline

N, M = map(int, read().split(' '))
K = list(map(int, read().split(' ')))
C = []

for i in range(len(K)):
  if i == 0:
    C.append(K[0])
  else:
    C.append(K[i] + C[i - 1])

for _ in range(M):
  start, end = map(int, read().split(' '))
  print(C[end - 1] if start == 1 else C[end - 1] - C[start - 2])