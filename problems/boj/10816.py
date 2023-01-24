N = int(input())
an = list(sorted(map(int, input().split(' '))))
M = int(input())
am = map(int, input().split(' '))
ans = dict()

for n in an:
  if n in ans:
    ans[n] += 1
  else:
    ans[n] = 1

for n in am:
  if n in ans:
    print(ans[n], end=' ')
  else:
    print(0, end=' ')