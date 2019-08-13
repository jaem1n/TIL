def test_simple():
    assert total([1, 2, 3]) == 1 + 2 + 3
    assert total([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 4 + 5
    assert total([1, 1, 1, 1, 1]) == 1 + 1 + 1 + 1 + 1
    assert average([2, 4, 6]) == (2 + 4 + 6) / 3
    assert average([2, 4, 6, 8, 10]) == (2 + 4 + 6 + 8 + 10) / 5


scores = [80, 100, 70, 90, 40]


def total(scores):
    result = 0
    for i in scores:
        result += i
    return result


def average(scores):
    return total(scores) / len(scores)
