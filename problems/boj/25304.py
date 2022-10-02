import sys

read = sys.stdin.readline

X = int(read())
N = int(read())
s = 0

for i in range(N):
  a, b = map(int, read().split())
  s += int(a * b)

print('Yes' if X == s else 'No')