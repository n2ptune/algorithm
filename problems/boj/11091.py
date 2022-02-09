import sys

read = sys.stdin.readline

T = int(read())

for _ in range(T):
  a = [chr(i) for i in range(97, 123)]
  b = read().rstrip().replace(' ', '')
  b = list(
      map(
          lambda x: chr(ord(x) + 32) if ord(x) >= 65 and ord(x) <= 90 else x, b
      )
  )

  for ch in b:
    a = list(filter(lambda x: x != ch, a))

  if len(a):
    print('missing', ''.join(a))
  else:
    print('pangram')