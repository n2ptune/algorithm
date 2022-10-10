N = int(input())
primes = []
test = [False, False] + [True] * (N - 1)

for i in range(2, N + 1):
  if test[i]:
    primes.append(i)
    for j in range(2 * i, N + 1, i):
      test[j] = False

p = 0

while True:
  if len(primes) - 1 < p or N == 1:
    break
  if N % primes[p] == 0:
    print(primes[p])
    N = int(N / primes[p])
    p = 0
  else:
    p += 1