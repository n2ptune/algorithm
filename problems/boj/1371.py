lines = []
while True:
  try:
    line = input()
  except EOFError:
    break
  lines.append(line)

S = ''.join(lines).replace(' ', '')
ans = dict()

for ch in S:
  if not ans.get(ch):
    ans[ch] = 1
  else:
    ans[ch] += 1

m = max(ans.values())
f = list(filter(lambda x: x[1] == m, ans.items()))

print(''.join(sorted(list(map(lambda x: x[0], f)))))