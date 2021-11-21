import sys
read = sys.stdin.readline

eng_dic = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}
ar = []

M, N = map(int, read().split(' '))
T = list(range(M, N + 1))

for i in T:
  d = list(str(i))
  z = ''
  for ch in d:
    z += ' ' + eng_dic.get(ch)
  ar.append((z.strip(), i))

n = 10
ans = list(sorted(ar))
ans = [ans[i * n:(i + 1) * n] for i in range((len(ans) + n - 1) // n)]

for c in ans:
  s = list(map(lambda x: str(x[1]), c))
  print(' '.join(s))