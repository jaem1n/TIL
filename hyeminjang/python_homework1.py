
scores = [80, 100, 70, 90, 40]
# 합계
def total(score):
    return sum(score)
print(total(scores))

def total(n):
    sum = 0  # 질문 : sum의 위치
    for i in scores:
        sum += i
    return sum

print(total(scores))
scores = [80, 100, 70, 90, 40]

# 평균
def average(sum, list):
    return sum/len(list)
print(average(total(scores), scores))

# 질문 : return과 print의 차이

# 더하기

numbers = [1,3,5,7,9]
accumulator = 0
#1
for number in range (0,len(numbers)):
    accumulator += numbers[number]
print(accumulator)

#2
for number in numbers:
    accumulator += number
print(accumulator)

# 곱하기

numbers = [1,3,5,7,9]
accumulator = 1

#1
for i in range(0,len(numbers)):
    accumulator *= numbers[i]
print(accumulator)

#2

numbers = [1,3,5,7,9]
accumulator = 1

for i in numbers:
    accumulator *= i
print(accumulator)

# 구구단

for a in range(2,10):
    for b in range (1,10):
        print(a,'*',b,'=',a*b)

#function

def double (n):
    return n*2
print(double(1))

def add(x,y):
    return x+y
print(add(3,5))

def bmi(weight,height):
    """Calculate BMI(Body Mass Index) with weight and height.

    Parameters:
    weight: Body weight in kilograms.
    height: Body height in meters.
    """
    return weight / (height ** 2)
print (bmi(68,1.82))
print(bmi.__doc__)

#계승

def factorial(n):
    accumulator = 1
    for i in range(1,n+1):
        accumulator*= i
    return accumulator

for i in range(1,11):
    print(factorial(i))



class_scores = [
    [30, 90, 80, 40, 50],
    [100, 100, 100, 100, 100],
    [90, 90, 30, 30, 20]
]
# 합계

sum = 0
for i in class_scores:
    for j in i:
        sum += j
print(sum)

# 평균
# sum = 0
# for i in class_scores:
#     for j in i:
#         sum += j
# print(sum/len(j))

def sumscore(list):
    sum = 0
    for i in range(0,len(list)):
        for j in range(0,len(list[i])):
            sum += list[i][j]
        return sum
print(sumscore(class_scores)) #질문 : 완전 모르겠다