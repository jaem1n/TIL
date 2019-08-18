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
    assert scores[:-1] == [10, 20]

    scores.append(5)
    assert scores == [10, 20, 30, 5]
    #바꾸기
    scores[0] = 0
    assert scores == [0, 20, 30, 5]

def test_dictionary():
    scores = {
        '국어' : 10,
        '영어' : 20,
        '수학' : 30
    }
    assert scores['국어'] == 10
    assert scores['영어'] == 20
    assert scores['수학'] == 30
    #바꾸기
    scores['국어'] = 100
    assert scores['국어'] == 100



def test_dictionary2():
    korean = '국어'
    scores = {
        korean: 10,
        20: 15
    }
    assert scores[korean] == 10
    assert scores['국어'] == 10
    assert scores[20] == 15
    #새로운 것 추가
    scores['영어'] = 20
    assert scores['영어'] == 20

def test_set():
    subjects = {'국어', '영어', '수학'}
    assert '국어' in subjects
    assert '음악' not in subjects
    assert '음악' in subjects.union({'음악'})
    subjects.add('체육')
    assert '체육' in subjects


# union: 합집합
# list에서 추가할 땐 append
# 집합에서 추가할 때는 add
# set이랑 dictionary에서만 {중괄호}를 사용함


