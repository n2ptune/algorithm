K = input().rstrip()
ans = ''

for ch in K:
  if ord(ch) - 3 < 65:
    ans += chr(91 - (65 - (ord(ch) - 3)))
  else:
    ans += chr(ord(ch) - 3)

print(ans)