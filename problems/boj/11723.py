import sys
read = sys.stdin.readline

res = set()
T = int(read())

for _ in range(T):
  command = read().rstrip()
  j = 0

  if not command in ['all', 'empty']:
    j = int(command.split(' ')[1])
    command = command.split(' ')[0]
  
  if command == 'add':
    res.add(j)
  elif command == 'remove':
    res.discard(j)
  elif command == 'toggle':
    if j in res:
      res.discard(j)
    else:
      res.add(j)
  elif command == 'all':
    a = [res.add(k) for k in range(1, 21)]
  elif command == 'empty':
    res = set()
  else:
    print(1 if j in res else 0)