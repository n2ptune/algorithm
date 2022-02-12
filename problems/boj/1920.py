N = int(input())
ns = set(map(int, input().rstrip().split(' ')))
M = int(input())
ms = list(map(int, input().rstrip().split(' ')))

for n in ms:
  print(1 if n in ns else 0)