scores = [80, 100, 70, 90, 40]

def total(l):
    total_scores = 0
    for i in l:
        total_scores += i
    return total_scores

def average(l):
    return total(l) / len(l)

def test_simple():
    assert total(scores) == 380
    assert average(scores) == 76