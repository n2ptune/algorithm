import sys
read = sys.stdin.readline

N, M = map(int, read().split(' '))
A = {}
B = {}

for _ in range(N):
  A[read().rstrip()] = 1

for _ in range(M):
  B[read().rstrip()] = 1

ans = []

if N >= M:
  for k in B.keys():
    if A.get(k):
      ans.append(k)
else:
  for k in A.keys():
    if B.get(k):
      ans.append(k)

ans.sort()

print(len(ans))
print('\n'.join(ans))