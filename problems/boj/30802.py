import sys
read = sys.stdin.readline

N = int(read())
sizes = list(map(int, read().split(' ')))
T, P = map(int, read().split(' '))

tr = 0 # 티셔츠 묶음
pr = 0 # 펜 묶음
pj = 0 # 펜 낱개

for size in sizes:
  if size > 0:
    if T >= size:
      tr += 1
    elif size % T == 0:
      tr += size//T
    else:
      tr += size//T + 1

pr = N//P
pj = N % P

print(tr)
print("{0} {1}".format(pr, pj))
