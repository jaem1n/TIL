scores = [80, 100, 70, 90, 40]

total_sum = 0

def total(scores):
    total_sum = 0
    for i in range(0, len(scores)):
        total_sum += scores[i]
    return total_sum

def test_total():
    assert total(scores) == 380

def average(scores):
    avg = total(scores) / len(scores)
    return avg

def test_average():
    assert average(scores) == 76

