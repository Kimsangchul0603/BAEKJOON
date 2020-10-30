# 평균

# 세준이의 성적을 위의 방법대로 새로 계산했을 때,
# 새로운 평균을 구하는 프로그램을 작성하시오.

# 점수 list를 생성하고 list 중 최댓값을 추출 = list_score, max_score
# 일반적인 평균과 세준이의 계산법을 적용한 후 평균을 구한다. = before, after_average
# after_average 출력

N = int(input())

list_score = list(map(int, input().split()))
max_score = max(list_score)

before_average = sum(list_score) / N
after_average = before_average * 100 / max_score

print(after_average)