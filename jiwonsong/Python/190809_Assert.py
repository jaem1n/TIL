# def double():
#     # TODO : 작업해야 함.
#     pass

def double(n):
    return n * 2

assert double(2) == 4       # 자동화 : 틀린 line 을 알려줌
assert double(1234) == 2468

def test_simple():
    assert double(2) == 4
    assert double(3) == 6
    assert double(1234) == 2468

# 연습문제
# score 가 다음과 같은 형태로 주어졌을 때
# scores = [80,100,70,90,40]
# total, average 를 만들고자 합니다.
# 1. 테스트 코드 작성하기
# 2. TDD 로 함수 만들기
# 3. 코드를 Github 에 올리기
# 4. 코드 리뷰

scores = [80,100,70,90,40]

def total(scores):
    result = 0
    for i in scores:
        result += i
    return result

def average(scores):
    return total(scores) / len(scores)

def test_simple():
    assert total(scores) == 380
    assert average(scores) == 76
