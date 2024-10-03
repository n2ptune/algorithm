import sys
n, *a = map(int, sys.stdin.buffer.read().splitlines())
stack = []
res = []
b = 1

for t in a:
  while b <= t:
    stack.append(b)
    res.append('+')
    b += 1

  if stack.pop() == t:
    res.append('-')
  else:
    print('NO')
    res = []
    break
    
if len(res) >= 1:
  print('\n'.join(res))