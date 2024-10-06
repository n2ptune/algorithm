import sys
s = sys.stdin.buffer.read().splitlines()

def find_number(n):
  try:
    int(n)
    return True
  except:
    return False


z = list(filter(find_number, s))
diff = 3 - s.index(z[0])
t = int(z[0]) + diff

if t % 3 == 0 and t % 5 == 0:
  print('FizzBuzz')
elif t % 3 == 0:
  print('Fizz')
elif t % 5 == 0:
  print('Buzz')
else:
  print(t)