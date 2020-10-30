# OX 퀴즈

# 문제의 점수 : 연속된 O의 개수 점수
# OOXXOXXOOO의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
# 점수를 구하는 프로그램을 작성하시오.

N = int(input())

for i in range(N):
    score = input() # ox퀴즈 정보 입력받기
    current_score = 0 # 현재 점수, 연속된 o가 3개면 current_score = 3
    list_score = [0] * len(score) # 각 문제 별 점수 기록 리스트
    for j in range(len(score)):
        if score[j] == 'O':
            current_score += 1 # o이면 현재 점수가 1 증가
            list_score[j] = current_score # 해당 문제의 점수는 current_score
        else:
            current_score = 0 # x이면 현재 점수가 0으로 리셋
    sum_score = sum(list_score) # 각 문제 별 점수의 합
    print(sum_score)
