import sys
read = sys.stdin.readline

works = []


def rotate(r, direction):
    if r in [w[0] for w in works]:
        return

    works.append((r, direction))

    dx = [-1, 1]
    dd = 1 if direction == -1 else -1

    for x in dx:
        if 0 <= r + x < len(wheels):
            if (x < 0 and wheels[r - 1][2] != wheels[r][-2]) or (x > 0 and wheels[r][2] != wheels[r + 1][-2]):
                rotate(r + x, dd)


wheels = [list(map(int, list(read().rstrip()))) for _ in range(4)]

for _ in range(int(read())):
    w, d = list(map(int, read().split(' ')))

    rotate(w - 1, d)

    for r, direction in works:
        if direction == 1:
            wheels[r] = [wheels[r][-1]] + wheels[r][:-1]
        elif direction == -1:
            wheels[r] = wheels[r][1:] + [wheels[r][0]]

    works = []

print(sum([wheels[i][0] * (2 ** i) for i in range(4)]))
