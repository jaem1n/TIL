def test_list():
    scores = [10,20,30]
    assert scores[0] == 10
    assert scores[2] == 30
    assert scores[-1] == 30
    assert scores[:2] ==[10,20]
    assert scores[1:]==[20,30]
    assert scores[:-1]==[10,20] #앞부터 뒤꺼 전까지!

scores = [10,20,30]
scores.append(5)
assert scores == [10,20,30,5]
scores[0] = 0
assert scores == [0,20,30,5]

def test_dictionary():
    scores = {
        '국어': 10,
        '영어': 20,
        '수학': 30
    }

assert scores['국어'] == 10
assert scores['수학'] == 30

scores['국어'] == 100
assert scores['국어'] == 100

def test_dictionary2():
    korean = '국어'
    scores = {
        kroean : 10,
        20 : 15
    }
    assert scores[korean] == 10
    assert scores['국어'] == 10
    assert scores[20] == 15
    scores['영어'] = 20
    assert scores['영어'] == 20
    scores['영어'] = 30
    assert scores['영어'] == 30






