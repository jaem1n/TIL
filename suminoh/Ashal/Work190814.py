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


def total_all(scores):
    total = 0
    for i in range(len(scores)):
        for j in scores[i]:
            total += scores[i][j]
    return total


def total_class(scores, subject):
    total = 0
    for i in range(len(scores)):
        total += scores[i][subject]
    return total


def test_total_all():
    assert total_all([]) == 0
    assert total_all([{'국어': 80, '영어': 100, '수학': 50}]) == 230
    assert total_all([{'국어': 90, '영어': 70, '수학': 40}]) == 200
    assert total_all([{'국어': 80, '영어': 100, '수학': 50},{'국어': 90, '영어': 70, '수학': 40}]) == 430


def test_total_class():
    assert total_class([], '국어') == 0
    assert total_class([{'국어': 80, '영어': 100, '수학': 50}], '국어') == 80
    assert total_class([{'국어': 80, '영어': 100, '수학': 50},{'국어': 90, '영어': 70, '수학': 40}], '국어') == 170
    assert total_class([{'국어': 80, '영어': 100, '수학': 50},{'국어': 90, '영어': 70, '수학': 40}], '영어') == 170
    assert total_class([{'국어': 80, '영어': 100, '수학': 50},{'국어': 90, '영어': 70, '수학': 40}], '수학') == 90
