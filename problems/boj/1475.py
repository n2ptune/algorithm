a = [0 for i in range(10)]
s = list(map(int, input()))

for ch in s:
  n = int(ch)
  if n == 6 or n == 9:
    a[6] += 1
  else:
    a[n] += 1

if a[6] % 2 == 0:
  a[6] = a[6] // 2
else:
  a[6] = a[6] // 2 + 1

print(max(a))