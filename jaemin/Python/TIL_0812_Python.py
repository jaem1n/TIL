# 점수 합계 TDD

def total(scores):
    # return scores[0]

    # total_score = 0
    # total_score += scores[0]
    # return total_score

    total_score = 0
    for i in range(0,len(scores)):
        total_score += scores[i]
    return total_score

def test_total_only_one():
    assert total([80]) == 80
    assert total([20]) == 20

def total2(scores):
    #return scores[0] + scores[1]

    total_score = 0
    for i in range(0,2):
        total_score += scores[i]
    return total_score

def test_total2_with_two_subjects():
    assert total2([80, 20]) == 100

def test_total_with_large_case():
    assert total([80, 20, 60, 70, 30]) == 80+20+60+70+30
    assert total([80, 20, 60, 70, 30]) == total([80, 20, 60, 70]) + 30
    assert total([80, 20, 60, 70, 30]) == total([80, 20, 60]) + 100


# 구구단 TDD

for i in range(1, 9+1):
    print(2, '*', i,'=', 2*i)

def multiply(x,y):
    # return '2 * 1 = 2'
    return f'{x} * {y} = {x * y}'   # formating

def multiplication_table():
    # return ['2 * 1 = 2', '2 * 2 = 4']

    # 초기값
    # multiplication = []
    # 누산
    # multiplication.append(multiply(2,1))
    # multiplication.append(multiply(2,2))

    multiplication = []
    for i in range(1,9+1):
        multiplication.append(multiply(2,1))
        multiplication.append(multiply(2,2))
        multiplication.append(multiply(2,3))
    return multiplication

def test_multiplication_table():
    assert multiply(2,1) == '2 * 1 = 2'
    assert multiply(2,2) == '2 * 2 = 4'

def test_multiplication_table():
    table = multiplication_table()
    assert table[0] == '2 * 1 = 2'
    assert table[1] == '2 * 2 = 4'


# Collection Element
# - list: 순서가 있음. key가 번호. key가 빠짐없이 연결됐다는 것을 보장. []로 만듦.
# - dictionary: key와 value가 짝을 이룸. {}로 만듦.
# - set: 집합(요소들을 모아둔 것). 중복을 허용하지 않는 리스트. {}로 만ㄷ름.
#        집합 연산을 위해 사용 (리스트에서는 값을 제거해버리는 것만 가능하고 차집합 불러오는게 불가능)
#        SQL에서 쿼리 자체가 집합

def test_list():
    scores = [10, 20, 30]
    assert scores[0] == 10
    assert scores[1] == 20
    assert scores[2] == 30
    assert scores[-1] == 30
    assert scores[-2] == 20
    assert scores[:2] == [10, 20]
    assert scores[1:] == [20, 30]
    assert scores[1:2] == [20]
    # append 실험
    scores.append(5)
    assert scores == [10, 20, 30, 5]
    # element 바꾸기
    scores[0] = 0
    assert scores == [0, 20, 30, 5]

def test_dictionary():
    scores = {
        '국어': 10,
        '영어': 20,
        '수학': 30
    }
    assert scores['국어'] == 10
    assert scores['영어'] == 20
    assert scores['수학'] == 30
    # element 바꾸기
    scores['국어'] = 100
    assert scores['국어'] == 100

def test_dictionary2():
    korean = '국어'
    scores = {
        korean: 10,
        20: 15
    }
    # 변수 바꿔치기
    assert scores[korean] == 10
    assert scores['국어'] == 10
    assert scores[20] == 15
    # 새로운 것 추가
    scores['영어'] = 20
    assert scores['영어'] == 20

def test_set():
    subjects = {'국어', '영어', '수학'}
    assert '국어' in subjects
    assert '음악' not in subjects
    assert '음악' in subjects.union({'음악'})  # subjects와 {'음악'}과의 합집합에서 찾기
    subjects.add('체육')
    assert '체육' in subjects