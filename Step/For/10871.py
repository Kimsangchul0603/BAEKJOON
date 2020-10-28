# x보다 작은 수
import sys

n, x = input().split()
n = int(n)
x = int(x)

num_list = list(map(int, input().split()))

for i in range(n):
    if num_list[i] < x:
        print(num_list[i], end=' ')
