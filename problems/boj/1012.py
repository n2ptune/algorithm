from collections import deque
import sys
read = sys.stdin.readline

T = int(read())

def visit(v, x, y):
  q = deque()
  q.append([x, y])
  v[y][x] = 0

  while q:
    nx, ny = q.popleft()
    step = []
    if nx + 1 < len(v[0]): step.append([nx + 1, ny])
    if not nx - 1 == -1: step.append([nx - 1, ny])
    if ny + 1 < len(v): step.append([nx, ny + 1])
    if not ny - 1 == -1: step.append([nx, ny - 1])
    
    for ax, ay in step:
      if v[ay][ax] == 1:
        v[ay][ax] = 0
        q.append([ax, ay])


for i in range(T):
  M, N, K = map(int, read().split(' '))
  v = []
  ans = 0

  for _ in range(N):
    v.append([0] * M)

  for j in range(K):
    x, y = map(int, read().split(' '))
    v[y][x] = 1

  for y in range(N):
    for x in range(M):
      if v[y][x] == 1:
        visit(v, x, y)
        ans += 1
  
  print(ans)