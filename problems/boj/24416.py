T = int(input())
a, b = [1, T - 2]
f = [0, 0, 0, 0, 0, 5, 8, 13]

while len(f) <= T:
  f.append(f[-1] + f[-2])

print("{0} {1}".format(f[T], b))
