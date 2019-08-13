# 팩토리얼
def factorial(n):
    accumulator = 1
    for i in range(1, n + 1):
        accumulator *= i
    return accumulator


print(factorial(3))


# 덧셈
def add(x, y):
    return x + y


print(add(1, 10))


# 2배
def double(a):
    return a * 2


print(double(10))


# BMI
def bmi(w, h):
    return w / h ** 2


print(bmi(50, 150))


# 구구단
def nbyn(n):
    print(n, "단")
    for i in range(1, 10):
        print(n, '*', i, '=', n * i)


nbyn(8)
