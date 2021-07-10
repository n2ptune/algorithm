import sys
read = sys.stdin.readline

N = int(read())

if not N % 2 == 0:
  print('a' * int(N / 2) + 'b' + 'a' * int(N / 2))
else:
  print('a' * N)