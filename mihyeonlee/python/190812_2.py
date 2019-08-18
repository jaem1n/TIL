#1. total 함수
#2. average 함수
# def total(scores):
#     return scores[0] + scores[1]
#
# def test_total_only_one():
#     assert total([80]) == 80
#     assert total([20]) == 20
#
# def test_total_with_two_subjects():
#     assert total([80, 20]) == 100
#
# def test_total_with_large_case():
#     assert total([80, 20, 60, 70, 30]) == 80 + 20 + 60 + 70 + 30
#     assert total([80, 20, 60, 70, 30]) == total([80, 20, 60, 70]) + 30
#     assert total([80, 20, 60, 70, 30]) == total([80, 20, 60]) + total([70, 30])

#############################################################
#구구단

# 2*1=2
# 2*2=4
# 2*3=6
# ...
# 9*8=72
# 9*9=81

# for i in range(1, 9+1):
#     print(2, '*', 1, '=', 2*1)

def multiply(x,y):
    return f'{x} * {y} = {x*y}'

def multiplication_table():
    multiplication = []
    for i in range(1, 9 + 1):
        multiplication.append(multiply(2, 1))
        multiplication.append(multiply(2, 2))
        multiplication.append(multiply(2, 3))
    return multiplication

def test_multiply():
    assert multiply(2,1) == '2 * 1 = 2'
    assert multiply(2,2) == '2 * 2 = 4'


def test_multiplication_table():
    table = multiplication_table()
    assert table[0] == '2 * 1 = 2'
    assert table[0] == '2 * 1 = 2'
############################################################




# def total_list(lists_name):
#     for i in range(len(class_scores)):
#         s = sum(class_scores[i])
#         print(s)
#
#
#
# def average_list(lists_name):
#     for i in range(len(class_scores)):
#         s = sum(class_scores[i])
#         print(s / len(class_scores[i]))
#
#
#
# def test_total_list():
#     assert total_list(class_scores) == 500
#
# def test_average_list():
#     assert averageg_list(class_scores) == 90


