T = int(input())

for _ in range(T):
  a, b = map(int, input().split(' '))
  print('NO BRAINS' if a < b else 'MMM BRAINS')