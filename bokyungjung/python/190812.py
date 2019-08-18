# class_scores dictionary set
class_scores = [ {
        '국어': 80,
        '영어': 100,
        '수학': 50
    },
    {
        '국어': 90,
        '영어': 70,
        '수학': 40
    }]

#특정 과목의 합계를 구하는 class_total 함수
def class_total(score, subject):
    total_score = 0
    for i in score:
        total_score += i[subject]
    return total_score

# class_total 함수 test
def test_class_total():
    assert class_total(class_scores, '국어') == 170
    assert class_total(class_scores, '영어') == 170
    assert class_total(class_scores, '수학') == 90

# class_total 함수 출력값 확인
print(class_total(class_scores, '국어'))

# class_scores의 모든 점수 구하는 함수
def class_total_all(score):
    total_all_score = 0
    for i in score:
        for j in i.values():
            total_all_score += j
    return total_all_score

# class_total_all 함수 test
def test_class_total_all():
    assert class_total_all(class_scores) == 430
    assert class_total_all([{1:10, 2:30}, {1:50, 2:90}]) == 180


# class_total_all 함수 출력값 확인
print(class_total_all(class_scores))
print(class_total_all([{1:10, 2:30}, {1:50, 2:90}]))

