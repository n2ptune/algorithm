from collections import deque

N, K = map(int, input().split(' '))
q = deque([i for i in range(1, N + 1)])
ans = []

while q:
  for i in range(K - 1):
    q.append(q.popleft())
  ans.append(q.popleft())

print('<{0}>'.format(', '.join(list(map(str, ans)))))