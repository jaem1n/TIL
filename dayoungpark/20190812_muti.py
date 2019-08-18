# 2*1=2
# 2*2=4
# 2*3=6
# ...
# 9*8=72
# 9*9=81


def multiply(x, y):
    return f'{x} * {y} = {x * y}'


def multiplication_table():
    # 초기값
    multiplications = []
    # 누산
    for i in range(1, 9 + 1):
        multiplications.append(multiply(2, i))
    return multiplications


def test_multiply():
    assert multiply(2, 1) == '2 * 1 = 2'
    assert multiply(2, 2) == '2 * 2 = 4'


def test_multiplication_table():
    table = multiplication_table()
    assert table[0] == '2 * 1 = 2'
    assert table[1] == '2 * 2 = 4'
    assert table[2] == '2 * 3 = 6'
    assert table[8] == '2 * 9 = 18'
