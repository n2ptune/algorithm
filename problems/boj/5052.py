import sys
read = sys.stdin.readline

T = int(read())

for _ in range(T):
  q = []
  N = int(read())
  for __ in range(N):
    q.append(read().rstrip())
  q.sort()
  flag = True
  for i in range(len(q) - 1):
    if q[i] == q[i+1][0:len(q[i])]:
      flag = False
      break
  print('YES' if flag else 'NO')
