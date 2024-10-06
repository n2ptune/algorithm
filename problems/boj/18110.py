import sys, queue
n, *a = map(int, sys.stdin.buffer.read().splitlines())
q = queue.deque(sorted(a))

def mround(n, digits = 0):
  mul = 10 ** digits
  return int(int(n * mul + 0.5) / mul)

m = mround(n * 15 / 100)

for i in range(m):
  q.popleft()
  q.pop()

print(mround(sum(q) / len(q)) if len(q) > 0 else 0)