# 평균은 넘겠지

# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 
# 당신은 그들에게 슬픈 진실을 알려줘야 한다.

# 1. 두번째 줄부터 점 리스트를 받아온다. = score_list
# 2. score_list의 첫 원소는 점수의 개수를 의미하기 때문에 값을 저장하고 리스트에서
#    제거한다. 점수의 개수 = score_list
# 3. score_list의 평균을 구하고 평균을 넘는 점수의 개수를 구한다. 
#    score_average, count
# 4. count와 score_num을 이용하여 비율을 구하고, 소숫점의 개수를 맞춰준다.

N = int(input())

for i in range(N):
    score_list = list(map(int, input().split()))
    score_num = score_list[0]
    count = 0
    del score_list[0]
    score_average = sum(score_list) / score_num

    for j in range(score_num):
        if score_list[j] > score_average:
            count += 1
        
    score_rate = '%0.3f' % float((count / score_num) * 100)
    print(score_rate, '%', sep='')

