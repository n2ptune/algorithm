T = int(input())
for i in range(T):
  ans = ' '.join(list(reversed(input().rstrip().split(' '))))
  print('Case #{0}: {1}'.format(i + 1, ans))
