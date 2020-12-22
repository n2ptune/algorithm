x, y = list(input())
# 이동할 거리
d = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [1, -2], [-1, 2], [1, 2]]
x = ord(x) - 97
y = int(y) - 1
ans = 0

for dx, dy in d:
  if x + dx >= 0 and y + dy >= 0:
    ans += 1

print(ans)