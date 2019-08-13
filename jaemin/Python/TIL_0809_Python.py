# test를 하는 방법
# 1. 이제까진 print해서 눈으로 확인했다.
# 2. 자동화되어서 출력하기 전에 틀린 걸 알려주면 좋겠다.
# 3. 어떻게 자동화하지? -> 단정문


# 단정문 (assertion)
assert 1+1 == 2  # 아무 일도 일어나지 않음 (패스)
assert 1+2 == 4  # assertion error

def double(n):
    return n * 2
     # 그냥 끝낼 때는 pass(아직 작업을 하지 않았다는 뜻), 또는 return 만 쓴다

print(double(2))
print(double(1))
print(double(1234))

# print로 찍으면 출력값을 직접 찾아야 함.
# assert로는 맞았는지 틀렸는지 바로 알 수 있음: 자동화

assert double(2) == 3
assert double(2) == 4
assert double(1) == 2
assert double(1234) == 2468


# pytest를 이용한 TDD : 테스트 함수를 짠 후 pytest로 돌려서 바로바로 확인

def test_simple():
    assert 1+1 == 2

def double(n):
     return n * 2

def test_double():
    assert double(2) == 4
    assert double(1) == 2
    assert double(1234) == 2468

