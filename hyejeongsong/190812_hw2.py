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


# 국어 성적 합

def class_total(class_scores,subject):
    scores = 0
    for i in range(0,len(class_scores)):
        scores += class_scores[i][subject]
    return scores

def test_class_total(class_scores,subject):
    assert class_total(class_scores, '국어') == 170



# 전체 성적 합

def class_total_all(class_scores):
    total_score = 0
    for i in class_scores:
        for j in i.values():
            total_score += j
    return total_score

def test_class_total_all(class_scores):
    assert class_total_all(class_scores) == 430
    assert class_total_all([{'국어:100'},{'영어:90'}]) == 190
