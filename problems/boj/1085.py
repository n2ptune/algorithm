x, y, w, h = map(int, input().split(' '))
print(min([x - 0, y - 0, w - x, h - y]))