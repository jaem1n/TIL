def test_set():
    subjects = {'국어','영어','수학'}
    other_subjecs = {'영어','음악'}
    assert '국어' in subjects
    assert '음악' not in subjects
    subjects.add('체육')
    assert '체육' in subjects

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

def class_total(class_scores, subject):
    total = 0
    for i in range(0,len(class_scores):
        total += class_scores[i][subject]
    return total

assert class_total(class_scores,'국어') == 170

def class_total_all(class_scores):
    total = 0
    for i in class_scores:
        for j in i.vlause():
            total += j
    return total

assert class_total_all(class_scores) == 430

def test_class_total_all(class_scores):
    assert class_total_all(class_scores) == 430
    assert class_total_all([{'국어:100'},{'영어:90'}]) == 190