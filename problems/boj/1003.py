f = [0, 1, 1]
fz = [(1, 0), (0, 1), (1, 1)]

for _ in range(int(input())):
  t = int(input())

  if not len(f) - 1 > t:
    for i in range(t - (len(f) - 1)):
      la, lb = fz[-2]
      lc, ld = fz[-1]

      fz.append((la + lc, lb + ld))
      f.append(f[-2] + f[-1])

  sx, sy = fz[t]
  print(sx, sy, sep=' ')
