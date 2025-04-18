import sys
read = sys.stdin.readline

N = int(read())
lope = []
result = []

for _ in range(N):
  lope.append(int(read()))
  
lope = list(sorted(lope))

for i, l in enumerate(lope):
  result.append(l * (N - i))

print(max(result))