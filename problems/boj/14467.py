ans = 0
m = {}

for i in range(int(input())):
  n, d = map(int, input().split(' '))

  if not n in m:
    m[n] = d
  elif m[n] != d:
    m[n] = d
    ans += 1

print(ans)