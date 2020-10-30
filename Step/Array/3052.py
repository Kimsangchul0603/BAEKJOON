# 나머지

# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 
# 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

# 입력값을 42로 나눈 값을 모아서 list 생성 = num_list
# 중복값을 제거하기 위해 list를 set으로 변환
# 변환된 set 원소의 개수를 출력

num_list = []

for i in range(10):
    num_list.append(int(input()) % 42)

set_num_list = set(num_list)
print(len(set_num_list))