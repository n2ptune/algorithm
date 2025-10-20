import sys
read = sys.stdin.readline

N, M = map(int, read().split())
A = [list(map(int, read().split())) for _ in range(N)]
M, K = map(int, read().split())
B = [list(map(int, read().split())) for _ in range(M)]
ans = []

for i in range(N):
    q = []
    for j in range(K):
        t = sum(A[i][k] * B[k][j] for k in range(M))
        q.append(t)
    ans.append(q)

for c in ans:
    print(*c, sep=' ')
