ans = dict()
S = input().rstrip()

for i in range(0, len(S)):
  if len(S) - 1 == i:
    ans[S] = 1

  for j in range(0, len(S)):
    if j+i+1>len(S): break
    c = S[j:j+i+1]
    ans[c] = 1


print(len(ans.keys()))