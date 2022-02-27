import sys
read = sys.stdin.readline

ha = {}

N, M = map(int, read().split(' '))

for i in range(N):
  ha[read().rstrip()] = i + 1

rha = dict(zip(ha.values(), ha.keys()))

for i in range(M):
  c = read().rstrip()

  try:
    a = int(c)
    print(rha[a])
  except:
    print(ha[c])
