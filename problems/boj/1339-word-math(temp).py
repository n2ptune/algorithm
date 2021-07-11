import sys
from queue import deque
read = sys.stdin.readline

N = int(read())
nums = deque(list(range(9, -1, -1)))
wordMap = {}
pool = []

for _ in range(N):
  pool.append(read().rstrip())

pool = sorted(pool, key=lambda x: len(x), reverse=True)
ls = list(filter(lambda x: not len(x) == len(pool[0]), pool))
pool = list(filter(lambda x: len(x) == len(pool[0]), pool))

for s in ls:
  c = '0' * (len(pool[0]) - len(s))
  pool.append(c + s)

npool = []

for i, S in enumerate(pool):
  ntemp = ''
  for j, ch in enumerate(S):
    if not wordMap.get(ch):
      if not i == len(pool) - 1:
        if len(pool[i + 1]) - 1 > j and not pool[i + 1][j] == '0':
          n = nums.popleft()
          wordMap[pool[i + 1][j]] = n
        m = nums.popleft()
        wordMap[ch] = m
        ntemp += str(m)
    else:
      ntemp += str(wordMap.get(ch))
  npool.append(int(ntemp))
  #   if not wordMap.get(ch):
  #     n = nums.popleft()
  #     ntemp += str(n)
  #     wordMap[ch] = n
  #   else:
  #     ntemp += str(wordMap.get(ch))
  # npool.append(int(ntemp))

print(sum(npool), wordMap)