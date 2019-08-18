def class_dictroy():
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


first = class_scores[0]
second = class_scores[1]


# 1 assert class_total(class_scores, '국어') == 170

def test_total(x, y):
    x = class_scores[0][0]
    y = class_scores[1][0]
    return f'{x} + {y} = {x + y}'


def test_dic():
    assert class_total([0][0] + [1][0]) == 170
    assert class_total(class_scores, '국어') == 170


# 2. class_total_all(class_scores) == 430

def test_total_all(x, y):
    sum = 0
    for x in range(0, 3):
        for y in range(0, 3):
            sum += x + y
    return sum


'''def class_total_all(score):
    total_all_score = 0
    for i in score:
        for j in i.values():
            total_all_score += j
    return total_all_score
'''


def test_class_total_all():
    sum(class_scores) == 430
