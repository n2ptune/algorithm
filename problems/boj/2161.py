from queue import deque

N = int(input())
A = [i for i in range(N, 0, -1)]
q = deque(A)
st = []

while True:
  if len(q) < 1:
    break
  if len(q) == 1:
    st.append(q.pop())
    break

  st.append(q.pop())
  q.appendleft(q.pop())

print(' '.join(list(map(str, st))))