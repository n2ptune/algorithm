t = int(input())
res = 0
c = 0

while t > c:
  res += 1
  
  if res == 1:
    c = 1
  else:
    c += 6 * (res - 1)

print(res)