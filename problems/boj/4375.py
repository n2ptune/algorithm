lines = []
while True:
  try:
    line = input().rstrip()
  except EOFError:
    break
  lines.append(line)

for s in lines:
  f = int('1' * len(s))

  if int(s) >= f and f % int(s) == 0:
    print(len(str(f)))
  else:
    i = len(s) + 1
    while True:
      g = int('1' * i)

      if g % int(s) == 0:
        break

      i += 1
    print(i)
