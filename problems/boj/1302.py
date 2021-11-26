import sys
read = sys.stdin.readline

h = {}

for _ in range(int(read())):
  c = read().rstrip()
  if not h.get(c):
    h[c] = 1
  else:
    h[c] += 1

m = max(list(h.values()))
h = list(h.items())
b = list(sorted(list(filter(lambda x: x[1] == m, h)), key=lambda x: x[0]))

print(b[0][0])