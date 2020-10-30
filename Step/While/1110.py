# 더하기 사이클

N = int(input())
new_N = N
cycle = 0

while True:
    cycle += 1
    
    new_left = new_N % 10
    new_right = ((new_N // 10) + (new_N % 10)) % 10
    new_N = 10 * new_left + new_right

    if new_N == N:
        break

print(cycle)
    