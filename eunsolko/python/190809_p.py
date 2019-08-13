scores = [80, 100, 70, 90, 40]


def total(score):
    t_scores = 0
    for i in score:
        t_scores += i
    return t_scores


def average(score):
    return total(score) / len(score)


def test():
    assert total(scores) == 380
    assert average(scores) == 76


test()
