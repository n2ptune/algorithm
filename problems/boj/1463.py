T = int(input())
s = dict({
  1: 0,
  2: 1,
  3: 1
})

if T in s:
  print(s[T])
else:
  for i in range(4, T + 1):
    if i % 3 == 0 and i % 2 == 0:
      s[i] = 1 + min(s[i - 1], s[i // 3], s[i // 2])
    elif i % 3 == 0 and i % 2 != 0:
      s[i] = 1 + min(s[i - 1], s[i // 3])
    elif i % 2 == 0 and i % 3 != 0:
      s[i] = 1 + min(s[i - 1], s[i // 2])
    else:
      s[i] = 1 + s[i - 1]
  print(s[T])