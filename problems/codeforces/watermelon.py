# https://codeforces.com/problemset/problem/4/A
W = int(input())

if W == 1 or W == 2:
  print('NO')
else:
  if W % 2 != 0:
    print('NO')
  else:
    print('YES')