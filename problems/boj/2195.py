from collections import deque
import sys

read = sys.stdin.readline

S, P = [read().rstrip() for _ in range(2)]
P = deque(P)
ans = 0
temp = ''

while P:
    temp += P.popleft()
    if temp in S:
        continue
    else:
        ans += 1
        P.appendleft(temp[-1])
        temp = ''

if temp:
    ans += 1

print(ans)