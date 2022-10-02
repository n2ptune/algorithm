v = [1, 1, 2, 2, 2, 8]
inp = list(map(int, input().split(' ')))
r = []

for i in range(0, 6):
  r.append(v[i] - inp[i])

print(' '.join(list(map(str, r))))