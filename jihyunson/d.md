1. total function 만들기
2. average 함수 만들기
3. 제대로 했는지 확인
4. github


## 1번
```py
scores = [80, 100, 70, 90, 40]
def all(scores):
    total = 0
    for i in range(0, len(scores)):
        total += scores[i]
    return(total)
print (all(scores))
```

## 2번
```py
scores = [80, 100, 70, 90, 40]
def average(scores):
    total = 0
    for i in range(0, len(scores)):
        total += scores[i]
        answer = total/len(scores)
    return(answer)
print (average(scores))
```