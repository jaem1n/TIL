# 과제
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

# Q1. class_total(class_scores, '국어') == 170

first = class_scores[0]
second = class_scores[1]

def class_total(class_scores, x):
    return first[x] + second[x]

def test_dic():
    assert class_total(class_scores, '국어') == 170

# Q2. class_total_all(class_scores) == 430

def class_total_all(class_scores):
    total = 0
    for i in list(first.keys()):
        total += class_total(class_scores, i)
    return total

def test_dic_all():
    assert class_total_all(class_scores) == 430
