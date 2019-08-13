```py
my_scores = [30, 90, 80, 40,50]
class_scores = 
[30, 90, 80, 40, 50]
[100, 100, 100, 100, 100]   
[0, 90, 30, 30, 20]
```

Answer:
```py
my_scores = [30, 90, 80, 40, 50]
sum = 0
for i in range(0, len(my_scores)):
    sum += my_scores[i]
print(sum)
```
* Identity Element, 항등원: 덧셈할 때는 초기값 0, 곱셈할 때는 초기값 1 

평균 Answer
```py
class_scores = [[30, 90, 80, 40, 50], [100, 100, 100, 100, 100], [0, 90, 30, 30, 20]]
sum = 0
for i in range(len(class_scores)):
    for j in range(len(class_scores[i])):
        sum += class_scores[i][j]
        average = sum/(len(class_scores[i])*len(class_scores))
print(average)
```
