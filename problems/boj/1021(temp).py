from collections import deque

N, M = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))
d = deque(range(1, N + 1))
cursor = d[0]
ans = 0

for n in nums:
  if cursor == n:
    d.popleft()
    cursor = d[0]
    continue
  elif max(d) - n > cursor - n:
    print(d, n, cursor, 'm')
    while not cursor == n:
      d.rotate(1)
      ans += 1
      cursor = d[0]
  else:
    print(d, n, cursor, 'mm')
    while not cursor == n:
      d.rotate(-1)
      ans += 1
      cursor = d[0]

print(ans)