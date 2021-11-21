import sys
read = sys.stdin.readline

X = list(read().rstrip())
cnt = 0
check = sum(list(map(int, X)))

if 10 > check:
  print(0, 'NO' if not check % 3 == 0 else 'YES', sep='\n')
  X = False

while X:
  v = sum(list(map(int, X)))
  cnt += 1
  if v >= 10:
    X = list(str(v))
  else:
    print(cnt, 'NO' if not v % 3 == 0 else 'YES', sep='\n')
    break