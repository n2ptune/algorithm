import sys
read = sys.stdin.readline

g = {
  'A+': 4.5,
  'A0': 4.0,
  'B+': 3.5,
  'B0': 3.0,
  'C+': 2.5,
  'C0': 2.0,
  'D+': 1.5,
  'D0': 1.0,
  'F': 0.0
}
aa = 0
ab = 0

for _ in range(20):
  a, b, c = read().rstrip().split(' ')
  if c == 'P':
    continue
  else:
    aa += (g[c] * float(b))
    ab += float(b)

if ab > 0:
  print(float(aa / ab))
else:
  print(0.000000)
