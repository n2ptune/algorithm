a = int(input())
s = 1
ans = 0
for i in range(1, a + 1):
  s *= i
for c in list(reversed(str(s))):
  if not int(c) == 0:
    break
  ans += 1
print(ans)