# 세자리수 곱셈 연산

a = int(input())
b = input()

num_1 = a * (int(b[2]))
num_2 = a * (int(b[1]))
num_3 = a * (int(b[0]))

num_sum = num_3 * 100 + num_2 * 10 + num_1

print(num_1)
print(num_2)
print(num_3)
print(num_sum)