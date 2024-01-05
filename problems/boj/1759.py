from itertools import combinations

def vowel(lst):
  vb = ['a', 'e', 'i', 'o', 'u']
  v = list(filter(lambda x: x in vb, lst))
  rv = list(filter(lambda x: x not in vb, lst))

  if len(v) == 0: return False
  if len(rv) < 2: return False

  return True

L, C = map(int, input().split(' '))
alpha = list(sorted(input().split(' ')))
result = []

for i in combinations(alpha, L):
  result.append(list(i))

result = list(filter(vowel, result))

for i in result:
  print(''.join(i))