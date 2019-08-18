def total(scores):
    total_score = 0
    for i in range(0, len(scores)):
        total_score += scores[i]
    return total_score


def test_total_with_empty():
    assert total([]) == 0


def test_total_only_one():
    assert total([80]) == 80
    assert total([20]) == 20


def test_total_with_two_subjects():
    assert total([80, 20]) == 100


def test_total_with_large_case():
    assert total([80, 20, 60, 70, 30]) == 80 + 20 + 60 + 70 + 30
    assert total([80, 20, 60, 70, 30]) == total([80, 20, 60, 70]) + 30
    assert total([80, 20, 60, 70, 30]) == total([80, 20, 60]) + total([70, 30])


def multiplication_table():
    # return ['2* 1 = 2', '2 * 2 = 4', '2 * 3 = 6']
    # inital value
    multiplication = []
    # accumulation
    for i in range(1, 10):
        multiplication.append(multiply(2, i))
    return multiplication


def multiply(x, y):
    return f'{x} * {y} = {x * y}'


def test_multiplication_table():
    table = multiplication_table()
    assert table[0] == '2 * 1 = 2'
    assert table[1] == '2 * 2 = 4'
    assert table[2] == '2 * 3 = 6'
    assert table[3] == '2 * 4 = 8'
    assert table[8] == '2 * 9 = 18'
