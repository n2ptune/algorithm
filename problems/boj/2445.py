N = int(input())
ans = []


def star(i: int):
  if N - 1 == i:
    ans.append('*' * N * 2)
  else:
    q = ('*' * (i + 1))
    r = q + (' ' * (N * 2 - q.count('*') * 2)) + q
    ans.append(r)


for i in range(0, N - 1):
  star(i)

for i in range(N - 1, -1, -1):
  star(i)

print('\n'.join(ans))