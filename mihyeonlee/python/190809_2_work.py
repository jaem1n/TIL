###연습문제###
scores = [80, 100, 70, 90, 40]
def total(list_name):
    accumulator = 0
    for i in range(0, len(list_name)):
        accumulator += list_name[i]
    return accumulator
def average(list_name):
    return total(list_name)/len(list_name)

def test_total():
    assert total(scores) == 400
# 실패가 나옴

def test_average():
    assert average(scores) == 76
# passed

""" 지난 숙제를 모두 TTD로 풀기♡"""
# 구구단 프로그램에 대한 테스트 코드 작성
