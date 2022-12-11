X = int(input())
bars = [64]

while sum(bars) > X:
  short = min(bars)
  bars.remove(short)
  short_div = int(short / 2)
  bars.append(short_div)

  if not sum(bars) >= X:
    bars.append(short_div)

print(len(bars))