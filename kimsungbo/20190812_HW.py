'''
1) 두 개의 dictionary에서 국어 점수의 총 합은?

=> assert class_total(class_scores, '국어') == 170
이렇게 확인할 수 있는 함수를 만들어보세요

2) class_scores set에 있는 모든 점수의 합은 얼마인가요? 역시 함수를 만들어보세요

=> assert class_total_all(class_scores) == 430

'''

class_scores = [
    {
        '국어': 80,
        '영어': 100,
        '수학': 50
    },
    {
        '국어': 90,
        '영어': 70,
        '수학': 40
    }
]


def korean_total(scores):
    total_score = 0
    for i in scores:
        total_score += i.get('국어')
    return total_score


def class_total(scores):
    total_score = 0
    for i in scores:
        for j in i:
            total_score += i.get(j)
    return total_score


print(korean_total(class_scores))
print(class_total(class_scores))
