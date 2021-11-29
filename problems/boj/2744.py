S = input()

def convert(ch):
  if ord(ch) >= 97 and ord(ch) <= 122:
    return chr(ord(ch) - 32)
  else:
    return chr(ord(ch) + 32)


print(''.join(list(map(convert, S))))