#1. total 함수
#2. average 함수
#3. 누산 - for
#4. 초기값

def total(scores):
    total_score = 0
    for i in range(0, len(scores)):
        total_score += scores[i]
    return total_score

def test_total_only_one():
    assert total([80]) ==80
    assert total([20]) == 20

def test_total_with_two_subjiect():
    assert total([80, 20]) == 100

def test_total_with_large_case():
    assert total([80, 20, 30, 70, 60]) == 80 + 20+ 60+ 70+ 30
    assert total([80, 20, 30, 70, 60]) == total([80 + 20+ 60+ 70]) + 30
    assert total([80, 20, 30, 70, 60]) == total([80 + 20+ 60]) + total([30+70])
