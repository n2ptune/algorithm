import sys
import math

read = sys.stdin.readline

A, B, V = list(map(int, read().split(' ')))
print(math.ceil((V - B) / (A - B)))