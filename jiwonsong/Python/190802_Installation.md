## Chocolatey & Pycharm installation
cmd as administrator

## For-Loop
* range(1,n+1) 에서 n+1 쓰는 이유 : 마지막 숫자는 생략하므로.

```python
factorial = 1

for x in range(1, n+1):
    factorial *= x
```

```python
factorial = 1

for x in [1,2,3]:
    factorial *= x
```

* TDD
* Code Review
* Pair Programming

## 연습문제
score 가 다음과 같은 형태로 주어졌을 때,
* scores = [80,100,70,90,40]
1. total_score 구하기
2. 제대로 했는지 확인하기
3. 코드를 GitHub 에 올리기

### Solution 1.
```python
f = 80

for i in [100,70,90,40]:
    f += i

print(f)
```
### Solution 2.
```python
scores = [80,100,70,90,40]
f = 0

for i in range(0,5):
    f += scores[i]

print(f)
```

## 과제
1. 성적 총합 & 평균 구하기
```python
my_scores = [30, 90, 80, 40, 50]

class_scores = [
    [30, 90, 80, 40, 50],
    [100, 100, 100, 100, 100],
    [90, 90, 30, 30, 20]
]
```

2. 구구단 출력하기
```python
2 * 1 = 2
2 * 2 = 4
…
9 * 8 = 72
9 * 9 = 81
```