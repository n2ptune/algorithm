N, M = map(int, input().split(' '))
P = list(map(int, input().split(' ')))
ans = []

for _ in range(M):
  user = input().split(' ')
  user_num = int(user[0])
  correct = user[1:]
  score = 0

  for i in range(N):
    if correct[i] == 'O':
      score += P[i]

  ans.append((user_num, score))

high_score = max(map(lambda x: x[1], ans))
ans = sorted(ans, key=lambda x: x[0])
ans = list(filter(lambda x: x[1] == high_score, ans))
print(ans[0][0], ans[0][1])