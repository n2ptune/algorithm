import sys
read = sys.stdin.readline


def ps(l):
  pre = []
  suf = []

  for i in range(0, len(l)):
    a = l[0:i + 1]

    if not a == l:
      pre.append(a)

    b = l[len(l) - 1 - i:]

    if b and not b == l:
      suf.append(b)

  result = ''

  for i, ch in enumerate(pre):
    if ch == suf[i]:
      result = ch

  return result


S = read().rstrip()
T = read().rstrip()
flag = False
# 일치
common = ''

for i in range(0, (len(S) - len(T)) + 1):
  r = S[i:i + len(T)]

  if r == T:
    flag = True
    break

  if common and not r.startswith(common):
    continue
  elif not common:
    # 공통 부분 검색
    for k in range(len(T), 1, -1):
      v = r[0:k]
      common = ps(v)
      print(common)

print(1 if flag else 0, common)
