# class_total
# class_total_all

def class_total(class_scores, subject):
    # pass
    # return 0

    # results = {
    #     0: 0,
    #     1: 100
    # }
    # return results[len(class_scores)]

    #total_score = 0
    # 누산
    #scores = class_scores[0]
    #total_score += scores[subject]
    #return scores[subject]

    for i in range(len(class_scores)):
        scores = class_scores[i]
        total_score += scores[subject]
        # total_score += scores.get(subject,0) 로 써도 됨
    return total_score

def test_class_total():
    # assert class_total([]) == 0
    # assert class_total([], '국어') == 0
    assert class_total([{'국어':100}], '국어') == 100
    assert class_total([{'국어':100}, {'국어':30}], '국어') == 100
    assert class_total([{'국어':100},
                        {'국어':30},
                        {'국어':80}
                        ], '국어') == 210
    assert class_total([{'국어': 100, '영어':100},
                        {'국어': 30, '영어':10},
                        {'국어': 80, '영어':80}
                        ], '국어') == 210
    assert class_total([{'국어': 100, '영어': 100},
                        {'국어': 30, '영어': 10},
                        {'국어': 80, '영어': 80}
                        ], '수학') == 0

def total_all():
    total_score = 0
    # for i in scores:
    #     total_score += scores[i]  # key값
    # for score in scores.values():
    #     total_score += score  # value값
    for k, v in scores.items():
        print(k,v)
        total_score += v  # (key,value)
    # weights = {'국어':2, '영어':1}  # 가중치 주기
    return total_score

def test_total_all():
    assert total_all({'국어':100}) == 100


def class_total_all():
    total_score = 0
    # for i in range(len(class_scores)):
    #     total_score += total_all(class_scores[i])
    for scores in class_scores:
        total_score += total_all(scores)
    return total_score

def test_class_total_all():
    assert class_total_all


