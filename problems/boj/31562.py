import sys
read = sys.stdin.readline

N, M = map(int, read().split())
V = []

for _ in range(N):
    A, B, *C = read().rstrip().split(' ')
    V.append((B, ''.join(C)))

for _ in range(M):
    A = ''.join(read().rstrip().split(' '))
    F = filter(lambda x: x[1].startswith(A), V)
    FL = list(F)
    
    if len(FL) == 1:
        print(FL[0][0])
    elif len(FL) == 0:
        print("!")
    else:
        print("?")