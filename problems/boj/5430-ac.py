import sys
from queue import deque
read = sys.stdin.readline

T = int(read())

for _ in range(T):
  command = read().rstrip().replace('RR', '')
  l = int(read())
  if l:
    li = deque(list(read()[1:-2].split(',')))
  else:
    temp = read()
    li = []
  flag = False
  reverse_flag = False
  if command.count('D') > l:
    flag = True
  else:
    for com in command:
      if com == 'R':
        reverse_flag = True if not reverse_flag else False
      else:
        if reverse_flag:
          li.pop()
        else:
          li.popleft()
  if flag:
    print('error')
  else:
    if reverse_flag:
      li.reverse()
    print('[' + ','.join(list(map(str, li))) + ']')