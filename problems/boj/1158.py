N, K = map(int, input().split(' '))
J = [i for i in range(1, N + 1)]
T = K - 1
ans = []

while len(J):
  if T >= len(J):
    T = T % len(J)
  else:
    ans.append(str(J.pop(T)))
    T += K - 1

print('<', ', '.join(ans), '>', sep='')