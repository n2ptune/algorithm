lines = ''

while True:
  try:
    line = input().rstrip()
  except EOFError:
    break
  lines += line

print(sum(map(int, lines.split(','))))
