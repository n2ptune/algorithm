s = int(input())
ans = 0

while s >= 0:
  if s % 5 == 0:
    ans += (s // 5)
    break
  s -= 3
  ans += 1

print(ans if s >= 0 else -1)