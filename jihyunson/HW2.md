## 성적 총합 & 평균 구하기

my_scores = [30, 90, 80, 40, 50]

class_scores = [
    [30, 90, 80, 40, 50],
    [100, 100, 100, 100, 100],
    [90, 90, 30, 30, 20]
]

1. First try: name 'total' is not defined
```py
def test_total():
    assert total([80]) == 80
```

2. Second try: total( ) takes 0 positional arguments but 1 was given
```py
def total():
    pass

def test_total():
    assert total([80]) == 80
```

3. Third try: assert None == 80
```py
def total(scores):
    pass

def test_total():
    assert total([80]) == 80
```

4. Fourth try
```py
def total(scores):
    return 80

def test_total():
    assert total([80]) == 80
```

5. Fifth try: PASSED
```py
def total(scores):
    return scores[0]

def test_total():
    assert total([80]) == 80
```

6. Sixth try: 80 != 180
```py
def total(scores):
    return scores[0]

def test_total():
    assert total([80]) == 80
    assert total([80, 100]) == 180
```

7. Seventh try
```py
def total(scores):
    total_score = 0
    for i inrange(0, len(scores)):
        total_scores += scores[i]
    return total_score/len(scores)

def test_total_with_empty():
    assert total 
```


## Factorial
n = 3
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)


1. Empty suite
```py
def fact(n):
    pass
```

2. N is not defined
```py
factorial = 1
for i in range(1, n+1):
    factorial *= i
```

3. Empty suite
```py
factorial = 1
for i in range(1, 4):
    factorial *= i
assert factorial == 6
```

4. Pass
```py
def fact(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial

def test_fact():
    assert fact(3) == 6
``` 


## 구구단 출력하기

for i in range(2,10):
   for j in range(1, 10):
       print(i, "x", j, "=", i*j)
   print("-"*20)

1. Empty suite
```py
def mult(n):
    pass
```

2. N is note defined
```py
def mult(n):
    for i in range(2, 3):
        print (n)

def test_mult():
    assert mult(n) == 2
```

3. Passed
```py
for i in range(1, 3):
    for j in range(1, 3):
        n = i*j
        print (i*j)

def test_mult():
    assert n == 4
```

4. 
```py
for i in range(1, 10):
    for j in range(1, 10):
        n = i*j
        print (i "x" j " is " n)
```

## 구구단
1. 
```py
print('2*1 = ', 2)
print('2*2 = ', 4)
print('2*3 = ', 6)
...
```

2. 
```py
for i in [1,2,3,4,5,6,7,8,9]:
    print(2, '*', i, '=',2*i)
def test_mult():
assert multiply(2, 1) == 2

def  multiply(x, y):
    return 2

def multiply(x, y):
    return f'{x} * {y} = 2{x * y}'
```

3. 
```py
def test_mult():
assert multiply(2, 1) == 2
assert multiply(2, 2) == 4
for i in range(1, 9+ 1):
    print(multiply(2, i))
```

4. 
```py
def mult_table():
    table = test_mult()
assert table[0] == '2 * 1 = 2'
assert table[1] == '2 * 2 = 4'
for i in range(1, 9+ 1):
    print(multiply(2, i))

def mult_table():
    mult = []
    mult.append(mult(2, 1)
    mult.append(mult(2, 2))
    ...
    return mults