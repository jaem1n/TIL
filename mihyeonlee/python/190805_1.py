my_scores = [30, 90, 80, 40, 50]
class_scores = [
    [30, 90, 80, 40, 50],
    [100, 100, 100, 100, 100],
    [90, 90, 30, 30, 20]
]
print(sum(my_scores))
for i in range(len(class_scores)):
    s = sum(class_scores[i])
    print(i + 1, "번째 합계:", s)
    print(i + 1, "번째 평균:", s / len(class_scores[i]))
##########################################################
n = 3
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(str(n) + "!", "=", factorial)
########################################################
for x in range(2, 10):
    for i in range(1, 10):
        print(x, "*", i, "=", i * x)
##########################################################
x = int(input("몇 단을 보고 싶으신가요?"))
if x in range(2, 10):
    for i in range(1, 10):
        print(x, "*", i, "=", i * x)
else:
    y = int(input("1부터 9까지의 정수를 입력해주세요. 다시 물을게요. 몇 단을 보고 싶으신가요?"))
    if y in range(1, 9):
        for i in range(1, 10):
            print(y, "*", i, "=", i * y)
###################################################
scores = [80, 100, 70, 90, 40]
total_score = 0
for i in range(0, len(scores)):
    total_score += scores[i]
print(total_score)
###################################
"""다시해보기"""
# for scores in range(1, 5):
#     total_score += scores
#####################################
def factorial(n):
    accumulator = 1
    for x in range(1, n + 1):
        accumulator *= x
    return accumulator
print(factorial(1))
####################################
def double(n):
    return n * 2
print(double(1))
# 두배 만들기
######################################
numbers = [1, 3, 5, 7, 9]
accumulator = 0
for i in range(0, len(numbers)):
    accumulator += numbers[i]
print(accumulator)
#####################################
numbers = [1, 3, 5, 7, 9]
accumulator = 0
for i in numbers:
    accumulator += i
print(accumulator)
########################################
numbers = [1, 3, 5, 7, 9]
accumulator = 1
for i in range(0, len(numbers)):
    accumulator *= numbers[i]
print(accumulator)
########################################
numbers = [1, 3, 5, 7, 9]
accumulator = 1
for number in numbers:
    accumulator *= number
print(accumulator)
#########################################3
def add(x, y):
    return x + y
print(add(1, 3))
#########################################
def bmi(weight, height):
    return weight / (height ** 2)
print(bmi(68, 1.82))
###########################################3
def factorial(n):
    accumulator=1
    for i in range(1, n+1):
        accumulator *= i
    return accumulator
for i in range(1, 11):
    print(factorial(i))
########################################
#과제 1번 total 함수 만들기
scores = [80, 100, 70, 90, 40]
def total(list):
    accumulator = 0
    for i in range(0, len(list)):
        accumulator += list[i]
    return accumulator
print(total(scores))
#과제 2번 average 함수 만들기
def average(b):
    return total(b)/len(b)
print(average(scores))
