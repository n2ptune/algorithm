import sys

read = sys.stdin.readline

T = int(read())

for _ in range(T):
  s = read().rstrip().split(' ')
  print('god' + ''.join(s[1:]))