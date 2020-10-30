# 최소, 최대

# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

a = int(input())

num_list = list(map(int, input().split()))

num_max = max(num_list)
num_min = min(num_list)

print(num_min, num_max)