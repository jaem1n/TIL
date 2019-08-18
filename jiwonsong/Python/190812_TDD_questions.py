# 1. total 함수
# 2. average 함수
# 누산 - for
# 초기값

# Assignment 1

def total(scores):
    total_score = 0
    for i in range(0, len(scores)):
        total_score += scores[i]
    return total_score

def avg(scores):
    return total(scores) / len(scores)

def test_total_only_one():
    assert total([80]) == 80
    assert total([20]) == 20

def test_total_with_two_subjects():
    assert total([80, 20]) == 100

def test_total_with_large_case():
    assert total([80,20,60,70,30]) == 80 + 20 + 60 + 70 + 30
    assert avg([80,20,60,70,30]) == 52

# Assignment 2. 구구단

# 2*1=2
# 2*2=4
# 2*3=6
# ...
# 9*8=72
# 9*9=81

# for i in range(1, 9 + 1):
#     print(2, '*', i, '=', 2 * i)

def multiply(x,y):
    return f'{x} * {y} = {x * y}'

def multiplication_table():
    multiplications = []
    for i in range(1, 9 + 1):
        for j in range(2, 9 + 1):
            multiplications.append(multiply(i, j))
    return multiplications

print(multiplication_table())

------------------------------------------------

def test_list():
    scores = [10,20,30]
    assert scores[0] = 10
    assert scores[1] = 20
    assert scores[2] = 30
    assert scores[-1] = 30
    assert scores[:2] = [10,20]
    assert scores[1:] = [20,30]
    assert scores[:-1] = [10,20]
    # append 실행
    scores.append(5)
    assert scores == [10,20,30,5]

def test_dictionary():
    scores = {
                '국어': 10,
                '영어': 20,
                '수학': 30
    }
    assert scores['국어'] == 10
    assert scores['영어'] == 20
    assert scores['수학'] == 30

# 집합
def test_set():
    subjects = {'국어', '영어', '수학'}
    assert '국어' in subjects
    assert '음악' not in subjects
    subjects.add('체육')
    assert '음악' in subjects.union({'음악'}) # 합집합
