# [오늘 배운 것] assert



## 단정문

**1. assert 사용법**
```python
assert 1 + 1 == 2
# 아무 일도 일어나지 않음.

assert 1 + 2 == 2
# AssertionError 발생!

# 답인지 아닌지 확인하는 것과 비슷
```

**2. Double 만들기**
```python
def double(n):
    return n * 2

assert double(2) == 4

# 결과 값 = 아무일도 일어나지 않음(정답이라는 뜻)
```
**3. pytest**
```python
def test_simple():
    assert  1 + 1 == 3

# Run pytest하면 오류가 무엇인지 구체적으로 알 수 있다
```


-----------------------------------------------------------------
# Python 연습문제 풀이
## " 지금까지 배운 내용을 assert를 이용해 확인해보자 "
> Double
```python
def double(n):
    return n * 2

def test_double():
 assert double(2) == 4
 assert double(4) == 8
 assert double(10) == 20
```
> scores = [80, 100, 70, 90, 40] // Total 함수, Average 함수
```python
scores = [80, 100, 70, 90, 40]


def test_total():
    assert total([80]) == 80
    assert total([80, 30]) == 110
    assert total([80, 100, 70, 90, 40]) == 380


def test_avg():
    assert avg([80]) == 80
    assert avg([80, 30]) == 55
    assert avg([80, 100, 70, 90, 40]) == 76


def total(scores):
    total_score = 0
    for i in range(len(scores)):
        total_score += scores[i]
    return total_score


def avg(scores):
    return total(scores) / len(scores)
```
> 계승 구하기
```python
def test_total():
    assert total(2) == 2
    assert total(3) == 6
    assert total(4) == 24
    assert total(5) == 120

def total(n):
  factorial = 1
  for i in range(1, n + 1):
    factorial *= i
  return factorial
```
> 구구단

----> 아무리해도 정답이 안나와요ㅠㅠㅠ 8월 12일에 문제풀이 부탁드립니다ㅠㅠ






