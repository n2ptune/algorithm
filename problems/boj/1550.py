P = input()
ans = 0

for i, ch in enumerate(list(reversed(list(P)))):
  try:
    ans += int(ch) * (16**i)
  except:
    ans += (ord(ch) - 55) * (16**i)

print(ans)