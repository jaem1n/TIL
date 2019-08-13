# 누산 과정
# 1. 초기값 지정
# 2. 코드를 반복 입력 = 누산
# 3. 계산 결과 출력 및 확인

# TDD
# - Red
# - Green
# - Refactoring : for 문으로 표현

# 항등원: 더하기의 0, 곱하기의 1 (변수의 초기값으로 주는 것)



# < 8/2 숙제를 짝과 함께 여러 방식으로 다시 해 보기 >


my_scores = [30, 90, 80, 40, 50]

sum_m = 0

for i in my_scores:
    sum_m += i

avg_m = sum_m/len(my_scores)

print(sum_m)
print(avg_m)


for i in range(0, len(my_scores)):
    sum_m += my_scores[i]


class_scores = [
    [30, 90, 80, 40, 50],
    [100, 100, 100, 100, 100],
    [90, 90, 30, 30, 20]
]

sum_scores=[]
avg_scores=[]

for i in class_scores:
    sum_scores.append(sum(i))
    avg_scores.append(sum(i)/len(i))

print(sum_scores)
print(avg_scores)


sum_n = 0
avg_n = 0
num = 0

for i in class_scores:
    sum_n += sum(i)
    num += len(i)

avg_n = sum_n/num

print(sum_n, avg_n)

print((58+52+100)/3)


import statistics as stat

my_scores = [30, 90, 80, 40, 50]

avg = stat.mean(my_scores)
print(avg)


class_scores = [
    [30, 90, 80, 40, 50],
    [100, 100, 100, 100, 100],
    [90, 90, 30, 30, 20]
]

print(class_scores[0][1])

for i in class_scores:
    print(sum(i), sum(i)/len(i))


# -----------------------------------------------------------------------

# 추상화 abstraction : 많은 부분이 생략된다. 대신 고차원의 것들을 다룰 수 있음.
# --> 함수 function

n = 1
accumulator = 1
for x in range(1, n + 1):
    accumulator *= 1
print(accumulator)


def factorial(n):
    accumulator = 1
    for x in range(1, n + 1):
        accumulator *= x
    return accumulator

print(factorial(1))


def double(n):  # n: parameter
    return n * 2

print(double(1))  # 1: argument
print(double(2))


# < 8/2 숙제를 함수를 사용해서 다시 해 보기 >

# 구구단 함수로 표현

def gugudan(n):
    for i in range(1,10):
        print(n,"x",i,"=",n*i)
    return

gugudan(5)


# 점수 합계 & 평균을 함수로 표현

scores = [30, 90, 80, 40, 50]

class_scores = [
    [30, 90, 80, 40, 50],
    [100, 100, 100, 100, 100],
    [90, 90, 30, 30, 20]
]

result = 0

def scoress(list):
    for i in list:
        print(sum(i), sum(i)/len(i))
    return
scoress(class_scores)

def SumScore(list):
    sum = 0
    for i in range(0, len(list)):
        for j in range(0, len(list[i])):
            sum += list[i][j]
    return sum
print(SumScore(class_scores))
