from collections import deque

N, M = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))
d = deque(range(1, N + 1))
ans = 0

for n in nums:
  while True:
    if d[0] == n:
      d.popleft()
      break
    else:
      if len(d) / 2 > d.index(n):
        d.append(d.popleft())
        ans += 1
      else:
        d.appendleft(d.pop())
        ans += 1
print(ans)