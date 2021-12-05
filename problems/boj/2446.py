N = int(input())
ans = []


def star(i: int):
  s = int(((N * 2 - 1) - i) / 2)
  ans.append(' ' * s + '*' * i)


for i in range(N * 2 - 1, 0, -2):
  star(i)

for i in range(3, N * 2, 2):
  star(i)

print('\n'.join(ans))