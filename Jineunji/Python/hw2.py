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

def class_total(dic,key):
    total_subject=0
    for i in dic:
        total_subject+=i[key]
    return total_subject

def test_class_total():
    assert class_total(class_scores, '국어') == 170
    assert class_total(class_scores, '영어') == 170
    assert class_total(class_scores, '수학') == 90

def class_total_all(dic):
    total=0
    for i in dic:
        for j in i.values():
            total+=j
    return total

def test_class_total_all():
    assert class_total_all(class_scores) == 430