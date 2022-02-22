import sys

read = sys.stdin.readline

n = int(read())
nu = [int(read()) for _ in range(n)]
nu.sort()

for m in nu:
  print(m)