# 빠른 A+B

import sys
n = int(input())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)

# input과 비슷하지만 더 빨리 받아 올때 sys.stdin.readline()를 사용
# sys.stdin.readline()는 list형태로 받아온다.

# map : map(함수, 리스트) -> 리스트를 지정한 함수로 처리하여 보여준다.