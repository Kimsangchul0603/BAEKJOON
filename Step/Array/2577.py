# 숫자의 개수

# 세 개의 자연수 A, B, C가 주어질 때 A×B×C를 계산한 결과에 0부터 9까지
# 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

# 1. 각각의 숫자가 몇번 쓰였는지 count하는 list 생성 = list_count
# 2. 입력한 숫자들을 곱한 후 문자열로 변환 = target_num
# 3. target_num의 모든 자릿수를 지나는 for문 생성. 
#    자릿수가 n이면 list_count의 n번째 원소값이 1 증가
# 4. list_count 출력 

list_count = [0] * 10

a = int(input())
b = int(input())
c = int(input())

target_num = str(a * b * c)

for i in range(len(target_num)):
    list_count[int(target_num[i])] += 1

for i in range(10):
    print(list_count[i])

