## 1) 두 개의 dictionary에서 국어 점수의 총 합은?
=> assert class_total(class_scores, '국어') == 170 
이렇게 확인할 수 있는 함수를 만들어보세요

```py
class_scores = [
    {
        '국어': 80,
        '영어': 100,
        '수학': 50
    },
    {
        '국어': 90,
        '영어': 70,
        '수학': 40
    }
]

def test_Korean():
    class_scores = [
        {
            '국어': 80,
            '영어': 100,
            '수학': 50
        },
        {
            '국어': 90,
            '영어': 70,
            '수학': 40
        }
    ]
    assert class_scores[0] == {'국어': 80, '수학': 50, '영어': 100}
    one = class_scores[0]
    assert class_scores[1] == {'국어': 90, '수학': 40, '영어': 70}
    two = class_scores[1]
```
2. one = class_score[0], two = class_score[1]
```py
def total_Korean():
    assert dict.get(one, '국어') + dict.get(two, '국어') == 170
```


## 2) class_scores set에 있는 모든 점수의 합은 얼마인가요?
=> class_total_all(class_scores) == 430

```py
def test_Korean():
    class_scores = [
        {
            '국어': 80,
            '영어': 100,
            '수학': 50
        },
        {
            '국어': 90,
            '영어': 70,
            '수학': 40
        }
    ]
    assert class_scores[0] == {'국어': 80, '수학': 50, '영어': 100}
    one = class_scores[0]
    assert class_scores[1] == {'국어': 90, '수학': 40, '영어': 70}
    two = class_scores[1]

def class_total_all(class_scores):
    total = 0
    one = class_scores[0]
    two = class_scores[1]
    for i in one.values():
        total += i
    for i in two.values():
        total += i
    return total

def test_total_all():
    assert class_total_all(class_scores) == 430
```