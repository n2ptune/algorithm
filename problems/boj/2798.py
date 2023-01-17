N, M = map(int, input().split(' '))
A = list(filter(lambda x: x <= M, map(int, input().split(' '))))
A.sort(reverse=True)

ans = []

for i in range(len(A) - 1):
  for j in range(i + 1, len(A) - 1):
    for k in A[j + 1:]:
      ans.append(sum([A[i], A[j], k]))
print(sorted(filter(lambda x: x <= M, ans), reverse=True)[0])