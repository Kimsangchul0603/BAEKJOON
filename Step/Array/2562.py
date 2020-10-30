# 최댓값

# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째
# 수인지를 구하는 프로그램을 작성하시오.

num_list = []

for i in range(9):
    num_list.append(int(input()))

max_num = max(num_list)
max_index = num_list.index(max(num_list)) + 1  

print(max_num)
print(max_index)
