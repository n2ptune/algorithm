# https://codeforces.com/problemset/problem/71/A
N = int(input())

for _ in range(N):
  S = input()

  if len(S) <= 10:
    print(S)
  else:
    cnt = len(S[1:-1])
    ans = S[0] + str(cnt) + S[-1]
    print(ans)