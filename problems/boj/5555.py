import sys
read = sys.stdin.readline

T = read().rstrip()
N = int(read())
ans = 0

for _ in range(N):
  if (read().rstrip() * 2).count(T) > 0:
    ans += 1

print(ans)