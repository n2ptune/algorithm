n = int(input())
f = [0, 1, 1]

while len(f) - 1 < n:
  f.append(f[-1] + f[-2])

print(f[n])