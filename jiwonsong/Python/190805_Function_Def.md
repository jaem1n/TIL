## 연습문제
1. 초기값 지정
2. 누산

```python
total_score = 0
scores = [80,100,70,90,40]

for i in range(0, len(scores)):
    total_score += scores[i]

print(total_score)
```

## 과제
1. 성적 총합 & 평균 구하기
```python
# my_scores
my_scores = [30, 90, 80, 40, 50]
total_score = 0

for i in range(0, len(my_scores)):
    total_score += my_scores[i]
    average = total_score / len(my_scores)

print(total_score)
print(average)

# total_score
class_scores = [
    [30, 90, 80, 40, 50],
    [100, 100, 100, 100, 100],
    [90, 90, 30, 30, 20]
]
total_score = 0
total_length = 0

for i in range(len(class_scores)):
    for j in range(len(class_scores[i])):
        total_score += class_scores[i][j]
        total_length = len(class_scores[i]*len(class_scores))

print(total_score,total_score/total_length)
```

2. 구구단 출력하기
```python
for i in range(2,10):
    for j in range(1,10):
        print(i, "x", j, "=", i*j)
    print("-"*20)
```

# Function
1. Double
```python
def double(n):
    return n*2

print(double(1))
print(double(2))
```

2. Add
```python
def add(x,y):
    return x+y
print(add(1,3))
```

# 누산
1. 모두 더하기
```python
numbers = [1,3,5,7,9]
accumulator = 0
for i in range(len(numbers)):
    accumulator += numbers[i]
print(accumulator)
```
2. 모두 더하기2
```python
numbers = [1,3,5,7,9]
accumulator = 0
for number in numbers:
    accumulator += number
print(accumulator)
```
3. 모두 곱하기
```python
numbers = [1,3,5,7,9]
accumulator = 1
for i in range(len(numbers)):
    accumulator *= numbers[i]
print(accumulator)
```
4. 모두 곱하기2
```python
numbers = [1,3,5,7,9]
accumulator = 1
for number in numbers:
    accumulator *= number
print(accumulator)
```
5. 구구단
```python
for i in range(2, 9+1):
    for j in range(1, 9+1):
        print(i, '*', j, '=', i*j)
```
# 함수
1. 2배
```python
def double(n):
    return n*2
print(double(1))
print(double(2))
```
2. 더하기
```python
def add(x,y):
    return x+y
print(add(1,3))
```
3. BMI
```python
def bmi(weight, height):
    """Calculate BMI(Body Mass Index) with weight and height.

    Parameter:
    weight: Body weight in kilograms
    height: Body height in meters
    """
    return weight / (height ** 2)
print(bmi(68, 1.82))
```

4. 계승
```python
def factorial(n):
    accumulator = 1
    for i in range(1, n+1):
        accumulator *= i
    return accumulator

for i in range(1, 10+1):
    print(factorial(i))
```

## 과제
score 가 다음과 같은 형태로 주어졌을 때
scores = [80, 100, 70, 90, 40]
1. total 함수 만들기
2. average 함수 만들기
3. 제대로 했는지 확인하기
4. 코드를 GitHub 에 올리기

```python
def total(scores):
    total_score = 0
    for score in scores:
        total_score += score
    return total_score, total_score/len(scores)

print(total(scores))
```