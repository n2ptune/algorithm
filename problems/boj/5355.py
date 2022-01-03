for _ in range(int(input())):
  s = input().split(' ')
  x = float(s[0])
  cmd = s[1:]

  for c in cmd:
    if c == '@':
      x *= 3.0
    elif c == '%':
      x += 5.0
    else:
      x -= 7.0
  
  print("%.2f" % x)