import sys
import queue
read = sys.stdin.readline
T = int(read())

for i in range(T):
  N, M = map(int, read().split(' '))
  q = queue.deque(map(int, read().split(' ')))

  for index, j in enumerate(q):
    q[index] = [index, j]

  count = 1

  while len(q) > 0:
    index, k = q.popleft()
    flag = False
    
    for a, b in q:
      if b > k:
        q.append([index, k])
        flag = True
        break

    if flag: continue

    if index == M: break
    else: count += 1
    
  print(count)