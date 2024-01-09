ipv6 = input().rstrip()

def convert(s: str) -> str:
  return ':'.join(map(lambda x: ('0' * (4 - len(x))) + x if not len(x) == 4 else x, s.split(':')))

if not ipv6.count(':') == 7:
  start = ipv6.split('::')[0]
  end = ':' + ipv6.split('::')[1]
  tmp = ''

  while True:
    colon_count = start.count(':') + end.count(':') + tmp.count(':')
    if colon_count == 7: break

    tmp += ':0'

  tmp = start + tmp + end

  if tmp[0] == ':':
    tmp = '0' + tmp

  print(convert(tmp))
else:
  print(convert(ipv6))