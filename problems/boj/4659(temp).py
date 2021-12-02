import sys
import re
read = sys.stdin.readline
mr = re.compile('(a|e|i|o|u)')

def moeum(d):
  return mr.match(d)

def pprint(d, a):
  print('<', d, '>', ' is acceptable.' if a else ' is not acceptable.', sep='')

r = ''

while r != 'end':
  r = read().rstrip()

  if len(r) <= 2:
    if moeum(r) is None:
      pprint(r, False)